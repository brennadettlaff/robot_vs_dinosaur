
class Dinosaur:
    def __init__(self):
        self.name = "T-Rex"
        self.health = 100
        self.attack_power = 35


    def attack(self, robot):
        robot.health -= self.attack_power
        if robot.health < 0:
            print (f"{self.name} has attacked Robot for {self.attack_power} damage. {robot.name} has 0 health remaining.")
        else:
            print(f"{self.name} has attacked Robot for {self.attack_power} damage. {robot.name} has {robot.health} health remaining.")