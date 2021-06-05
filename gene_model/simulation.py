from abc import ABC
from random import getrandbits
from typing import List

from gene_model.chromosome import Chromosome, Individual


class Simulation(ABC):
    def __init__(self, population_size: int = 4):
        super().__init__()
        self.__initial_population: List[Individual] = []
        self.__population_size: int = population_size

    def _define_initial_population(self) -> List[Individual]:
        chromosome_length: int = 6
        base_chromosome: Chromosome = Chromosome(length=chromosome_length)
        initial_population: List[Individual] = []
        for ix in range(self.__population_size):
            for gene in range(chromosome_length):
                if bool(getrandbits(1)):
                    base_chromosome.flip_bit(gene)
            initial_population.append(
                Individual([Chromosome(genes=base_chromosome.get_genes())])
            )
        return initial_population

    @staticmethod
    def _fitness_phase():
        pass

    @staticmethod
    def _selection_phase():
        pass

    @staticmethod
    def _crossover_phase():
        pass

    @staticmethod
    def _mutation_phase():
        pass

    def run_simulation(self):
        self.__initial_population = self._define_initial_population()


class BasicSimulation(Simulation):
    def __init__(self):
        super().__init__()
