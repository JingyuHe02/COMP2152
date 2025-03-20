from character import Character


class Hero(Character):
    def __init__(self):
        super().__init__()

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()

    def hero_attacks(self, monster):
        damage = self.combat_strength
        print(f"Hero attacks Monster for {damage} damage!")
        monster.health_points -= damage
        if monster.health_points <= 0:
            print("Monster defeated!")
