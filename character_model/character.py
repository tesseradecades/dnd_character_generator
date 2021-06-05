from character_model.actions.attacks import UnarmedStrike


class Character:
    def __init__(self):
        self.__strength_score = 8

    def actions(self) -> list:
        return [UnarmedStrike(self.__get_modifier(self.__strength_score))]

    @staticmethod
    def __get_modifier(ability_score: int):
        return (ability_score - 10) / 2
