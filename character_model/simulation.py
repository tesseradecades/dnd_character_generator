from random import getrandbits
from typing import List

from character_model.character import Character
from gene_model.chromosome import Chromosome, Individual
from gene_model.simulation import Simulation


class DndSimulation(Simulation):
    def __init__(self, mutation_rate=0.5, population_size=4, starting_population=[]):
        super().__init__(
            mutation_rate=mutation_rate,
            population_size=population_size,
            starting_population=starting_population,
        )

    @staticmethod
    def _fitness_function(individual: Individual) -> int:
        character_representation: Character = Character(individual.get_chromosomes())
        return character_representation.get_actions()[0].get_damage()

    def _population_phase(self) -> List[Individual]:
        initial_population: List[Individual] = []
        for individual in range(self._population_size):
            initial_population.append(
                Individual([self.__generate_chromosome(6) for _ in range(27)])
            )
        return initial_population

    @staticmethod
    def __generate_chromosome(chromosome_length) -> Chromosome:
        return Chromosome(genes=[getrandbits(1) for _ in range(chromosome_length)])

    def get_characters(self) -> List[Character]:
        final_population: List[Individual] = self.run_simulation()
        return [
            Character(individual.get_chromosomes()) for individual in final_population
        ]
