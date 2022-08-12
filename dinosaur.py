
class Dinosaur:
    def __init__(self):
        self.name = "T-Rex"
        self.health = 100
        self.attack_power = 30


    def attack(self, robot):
        robot -= self.attack_power
        print(robot)