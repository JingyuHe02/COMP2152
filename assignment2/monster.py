from character import Character


class Monster(Character):
    def __init__(self):
        super().__init__()

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()

    def monster_attacks(self, hero):
        damage = self.combat_strength
        print(f"Monster attacks Hero for {damage} damage!")
        hero.health_points -= damage
        if hero.health_points <= 0:
            print("Hero has been defeated!")

