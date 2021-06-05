from abc import ABC
from typing import List


class Chromosome:
    def __init__(self, genes: List[int] = [], length: int = 0):
        if genes:
            self.__genes: List[int] = genes
        else:
            self.__genes: List[int] = [0] * length

    def __repr__(self):
        return self.get_genes()

    def flip_bit(self, index: int):
        value: int = self.__genes[index]
        if value:
            self.__genes[index] = 0
        else:
            self.__genes[index] = 1

    def get_genes(self) -> List[int]:
        return list(self.__genes)


class Individual(ABC):
    def __init__(self, chromosomes: List[Chromosome]):
        self._chromosomes: List[Chromosome] = chromosomes
        self.__fitness_score: int = 0

    def __repr__(self):
        return (
            f"Fitness Score:{self.get_fitness_score()}\tGenotype: {self.get_genes()}"
        )

    def get_genes(self) -> List[int]:
        all_genes: List[int] = []
        for chromosome in self._chromosomes:
            all_genes += chromosome.get_genes()
        return all_genes

    def get_chromosomes(self) -> List[Chromosome]:
        return list(self._chromosomes)

    def get_fitness_score(self) -> int:
        return int(self.__fitness_score)

    def set_chromosomes(self, chromosomes: List[Chromosome]):
        self._chromosomes = chromosomes

    def set_fitness_score(self, fitness_score: int):
        self.__fitness_score = fitness_score
