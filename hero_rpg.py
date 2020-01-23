#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"You do {self.power} damage to the enemy.")
        if enemy.health <= 0:
            print("The enemy is dead.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    pass

class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        return True

def main():

    hero = Hero(10, 5, "Rand al'Thor")
    goblin = Goblin(6, 2, "Goblin")
    zombie = Zombie(1, 1, "Zombie")

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

    print(f"""

Good job defeating the {goblin.name}, {hero.name}! A new enemy is approaching.....
    
    """)

    while zombie.alive() and hero.alive():
        print(f"\nIt's a showdown between the {zombie.name} and {hero.name}!\n")
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks zombie
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Smart move! They can't die you know.....")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if zombie.health > 0:
            # zombie attacks hero
            zombie.attack(hero)

main()
