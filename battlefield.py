from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.robot = Robot()

    def run_game(self):
        self.display_welcome()
        while self.robot.health >= 0 and self.dinosaur.health >= 0:
            self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur!")

    def battle_phase(self):
        self.robot.health = self.dinosaur.attack(self.robot.health)
        self.dinosaur.health = self.robot.attack(self.dinosaur.health)
        return(self.robot.health, self.dinosaur.health)

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print("Robot wins!")
        elif self.robot.health <= 0:
            print("Dinosaur wins!")