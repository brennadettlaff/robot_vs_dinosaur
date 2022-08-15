from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = "Robot"
        self.health = 100
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        dinosaur -= self.active_weapon.attack_power
        print(f"Robot has attacked Dinosaur with {self.active_weapon.name} for {self.active_weapon.attack_power} damage. Dinosaur has {dinosaur} health remaining.")
        return(dinosaur)
