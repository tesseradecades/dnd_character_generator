from character_model.character import Character
from gene_model.chromosome import Chromosome


class Test_get_actions:
    @staticmethod
    def test_empty_chromosome():
        # arrange
        character: Character = Character([])

        # act
        unarmed_strike_damage: int = character.get_actions()[0].get_damage()

        # assert
        assert unarmed_strike_damage == 0

    @staticmethod
    def test_high_strength_chromosome():
        # arrange
        character: Character = Character([Chromosome(genes=[1])] * 27)

        # act
        unarmed_strike_damage: int = character.get_actions()[0].get_damage()

        # assert
        assert unarmed_strike_damage == 3
