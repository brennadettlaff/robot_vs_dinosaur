from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.robot = Robot()

    def run_game(self):
        while self.robot.health >= 0 and self.dinosaur.health >= 0:
            self.battle_phase()

    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur!")

    def battle_phase(self):
        self.dinosaur.attack(self.robot.health)
        self.robot.attack(self.dinosaur.health)

    def display_winner(self):
        pass
