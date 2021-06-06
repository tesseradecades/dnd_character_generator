from abc import ABC
from copy import deepcopy
from random import getrandbits, randint
from typing import Callable, List, Tuple

from gene_model.chromosome import Chromosome, Individual
from gene_model.convergence_tests import hamming_distance


class Simulation(ABC):
    def __init__(
        self,
        mutation_rate: float = 0.5,
        population_size: int = 4,
        starting_population: List[Individual] = [],
    ):
        super().__init__()
        self.__current_max_fitness: int = 0
        self.__generations: int = 0
        self.__generations_without_fitness_increase: int = 0
        self.__mutation_rate: float = mutation_rate
        self.__population: List[Individual] = starting_population
        self._population_size: int = population_size

    @staticmethod
    def __sort_by_fitness(population: List[Individual]) -> List[Individual]:
        return sorted(population, reverse=True, key=lambda x: x.get_fitness_score())

    def __has_converged(
        self,
        previous_generation: List[Individual],
        current_generation: List[Individual],
    ) -> bool:
        total_genes_in_population: int = len(current_generation[0].get_genes()) * len(
            current_generation
        )
        target_hamming_distance: int = total_genes_in_population * self.__mutation_rate
        previous_generation_genes: List[int] = []
        for individual in self.__sort_by_fitness(previous_generation):
            previous_generation_genes += individual.get_genes()
        current_generation_genes: List[int] = []
        for individual in self.__sort_by_fitness(current_generation):
            current_generation_genes += individual.get_genes()
        criteria: List[bool] = [
            hamming_distance(previous_generation_genes, current_generation_genes)
            <= target_hamming_distance,
            self.__generations_without_fitness_increase >= total_genes_in_population,
            self.__generations >= total_genes_in_population ** 2,
        ]
        return sum(criteria) >= (len(criteria) / 2)

    @staticmethod
    def _fitness_function(individual: Individual) -> int:
        return sum([sum(c.get_genes()) for c in individual.get_chromosomes()])

    def _population_phase(self) -> List[Individual]:
        chromosome_length: int = 6
        base_chromosome: Chromosome = Chromosome(length=chromosome_length)
        initial_population: List[Individual] = []
        for ix in range(self._population_size):
            for gene in range(chromosome_length):
                if bool(getrandbits(1)):
                    base_chromosome.flip_bit(gene)
            initial_population.append(
                Individual([Chromosome(genes=base_chromosome.get_genes())])
            )
        return initial_population

    def __fitness_phase(self):
        for individual in self.__population:
            individual.set_fitness_score(self._fitness_function(individual))

    def __selection_phase(
        self,
    ) -> Tuple[Tuple[Individual, Individual], Tuple[Individual, Individual]]:
        sorted_population: List[Individual] = self.__sort_by_fitness(self.__population)
        fittest: Individual = sorted_population[0]
        max_fitness: int = fittest.get_fitness_score()
        if self.__current_max_fitness <= max_fitness:
            self.__generations_without_fitness_increase += 1
        else:
            self.__generations_without_fitness_increase = 0
        second_fittest: Individual = sorted_population[1]

        current_population_size: int = len(sorted_population)
        least_fit: Individual = sorted_population[current_population_size - 1]
        second_least_fit: Individual = sorted_population[current_population_size - 2]
        return ((fittest, second_fittest), (least_fit, second_least_fit))

    @staticmethod
    def _crossover_phase(
        reproducers: Tuple[Individual, Individual]
    ) -> Tuple[Individual, Individual]:
        parent_1_chromosomes: List[Chromosome] = reproducers[0].get_chromosomes()
        parent_2_chromosomes: List[Chromosome] = reproducers[1].get_chromosomes()

        child1_chromosomes: List[Chromosome] = list()
        child2_chromosomes: List[Chromosome] = list()

        for chromosome_index in range(len(parent_1_chromosomes)):
            p1_genes: List[int] = parent_1_chromosomes[chromosome_index].get_genes()
            p2_genes: List[int] = parent_2_chromosomes[chromosome_index].get_genes()

            crossover_point: int = randint(0, len(p1_genes))

            child1_genes: List[int] = (
                p1_genes[:crossover_point] + p2_genes[crossover_point:]
            )
            child1_chromosomes.append(Chromosome(genes=child1_genes))

            child2_genes: List[int] = (
                p2_genes[:crossover_point] + p1_genes[crossover_point:]
            )
            child2_chromosomes.append(Chromosome(genes=child2_genes))
        return (Individual(child1_chromosomes), Individual(child2_chromosomes))

    def __mutation_phase(self):
        for individual in self.__population:
            chromosomes: List[Chromosome] = individual.get_chromosomes()
            new_chromosomes: List[Chromosome] = list()
            for chromosome in chromosomes:
                new_chromosome: Chromosome = Chromosome(genes=chromosome.get_genes())
                for gene_ix in range(len(new_chromosome.get_genes())):
                    if randint(0, 100) < (100 * self.__mutation_rate):
                        new_chromosome.flip_bit(gene_ix)
                new_chromosomes.append(new_chromosome)
            individual.set_chromosomes(new_chromosomes)

    def run_simulation(self) -> List[Individual]:
        previous_generation: List[Individual] = list()
        if not self.__population:
            self.__population = self._population_phase()
        self.__generations = 1
        self.__fitness_phase()
        while not self.__has_converged(previous_generation, self.__population):
            previous_generation = deepcopy(self.__population)
            reproducers, recently_deceased = self.__selection_phase()
            offspring: Tuple[Individual, Individual] = self._crossover_phase(
                reproducers
            )
            self.__population.remove(recently_deceased[1])
            self.__population.remove(recently_deceased[0])
            self.__population.append(offspring[0])
            self.__population.append(offspring[1])
            self.__mutation_phase()
            self.__fitness_phase()
            self.__generations += 1
        return self.__population


class BasicSimulation(Simulation):
    def __init__(
        self, mutation_rate: float = 0.5, starting_population: List[Individual] = []
    ):
        super().__init__(
            mutation_rate=mutation_rate, starting_population=starting_population
        )
