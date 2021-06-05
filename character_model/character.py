from character_model.actions.attacks import UnarmedStrike
from gene_model.chromosome import Chromosome


class Character:
    def __init__(self, chromosomes: list):
        """
        Chromosomes
        [
            0:26 -> ability score chromosomes, each 6 bits in length
        ]
        """
        self.__charisma_score = 8
        self.__constitution_score = 8
        self.__dexterity_score = 8
        self.__intelligence_score = 8
        self.__strength_score = 8
        self.__wisdom_score = 8
        self.__chromosomes: list = chromosomes
        self.__assign_ability_scores()

    def __assign_ability_scores(self):
        points_applied: dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for chromosome in self.__chromosomes[:27]:
            points_applied[sum(chromosome.get_genes())] += 1
        print(points_applied)
        self.__strength_score += self.__render_added_score(points_applied[1])
        self.__dexterity_score += self.__render_added_score(points_applied[2])
        self.__constitution_score += self.__render_added_score(points_applied[3])
        self.__intelligence_score += self.__render_added_score(points_applied[4])
        self.__wisdom_score += self.__render_added_score(points_applied[5])
        self.__charisma_score += self.__render_added_score(points_applied[6])

    def __get_genes(self):
        all_genes: list = []
        for chromosome in self.__chromosomes:
            all_genes += chromosome.get_genes()

    @staticmethod
    def __get_modifier(ability_score: int) -> int:
        return (ability_score - 10) / 2

    @staticmethod
    def __render_added_score(applied_points: int) -> int:
        if applied_points < 1:
            return 0
        if applied_points <= 5:
            return applied_points
        if applied_points <= 9:
            return (applied_points + 5) / 2
        return 7

    def __str__(self):
        return f"Strength:\t{self.__strength_score}\nDexterity:\t{self.__dexterity_score}\nConstitution:\t{self.__constitution_score}\nIntelligence:\t{self.__intelligence_score}\nWisdom:\t{self.__wisdom_score}\nCharisma:\t{self.__charisma_score}"

    def __repr__(self):
        return f"{self.__str__()}\nGenotype:\t{self.__get_genes()}"

    def get_actions(self) -> list:
        return [UnarmedStrike(self.__get_modifier(self.__strength_score))]
