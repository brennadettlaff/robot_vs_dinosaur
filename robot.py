from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = "Robot"
        self.health = 100
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{self.name} has attacked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage. {dinosaur.name} has {dinosaur.health} health remaining.")
