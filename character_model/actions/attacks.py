from character_model.actions.actions import Action


class UnarmedStrike(Action):
    def __init__(self, ability_modifier: int, other_bonus: int = 0):
        super().__init__()
        self.damage: int = 1 + ability_modifier + other_bonus

    def get_damage(self) -> int:
        return int(self.damage)
