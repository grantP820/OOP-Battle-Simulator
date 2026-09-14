import random
class Hero:
    def __init__(self, name):
            self.name = name
            self.health = 150
            self.attack_power = 20
    def attack(self):
            return random.randint(10, self.attack_power)
    def take_damage(self, damage):
            self.health = max(0, self.health - damage)
            print(f"{self.name} takes {damage} damage. Health: {self.health}")
    def is_alive(self):
            return self.health > 0
    def battleCry(self):
           print("hero screams out to goblins intimiating the goblins")
    __init__
