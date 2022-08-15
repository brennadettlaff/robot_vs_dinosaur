from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.robot = Robot()

    def run_game(self):
        self.display_welcome()
        self.choose_weapon()
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur!")

    def battle_phase(self):
        self.dinosaur.attack(self.robot)
        self.robot.attack(self.dinosaur)

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f"{self.robot.name} wins!")
        elif self.robot.health <= 0:
            print(f"{self.dinosaur.name} wins!")

    def choose_weapon(self):
        self.robot.active_weapon.name = input(f"Choose a weapon for {self.robot.name}: Sword, Axe, or Spear.  ")
        if self.robot.active_weapon.name == "Sword" or self.robot.active_weapon.name == "sword":
            self.robot.active_weapon.attack_power = 35
        elif self.robot.active_weapon.name == "Axe" or self.robot.active_weapon.name == "axe":
            self.robot.active_weapon.attack_power = 40
        elif self.robot.active_weapon.name == "Spear" or self.robot.active_weapon.name == "spear":
            self.robot.active_weapon.attack_power = 25
        else:
            print("Please enter sword, axe, or spear to select a weapon")
        print(f"You have selected {self.robot.active_weapon.name} for {self.robot.name}.")