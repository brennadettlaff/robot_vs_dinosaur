from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = "Robot"
        self.health = 100
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        dinosaur -= self.active_weapon.attack_power
        print(dinosaur)
