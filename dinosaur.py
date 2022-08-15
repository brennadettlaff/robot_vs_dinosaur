
class Dinosaur:
    def __init__(self):
        self.name = "T-Rex"
        self.health = 100
        self.attack_power = 30


    def attack(self, robot):
        robot -= self.attack_power
        print(f"Dinosaur has attacked Robot for {self.attack_power} damage. Robot has {robot} health remaining.")
        return robot