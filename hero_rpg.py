
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} does {self.power} damage.")
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
    goblin = Goblin(6, 2, "The Goblin")
    zombie = Zombie(1, 1, "The Zombie")

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight the goblin.")
        print("2. Do nothing.")
        print("3. Flee the fight.")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if goblin.health > 0:
            goblin.attack(hero)
    print()
    print("*" * 40)
    print(f"""
Good job defeating the {goblin.name}, {hero.name}! A new enemy is approaching.....
    """)
    print("*" * 40)
    print()
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
            hero.attack(zombie)
            print("But what is dead may never die.....")
            zombie.attack(hero)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Smart move! They can't die you know.....")
            break
        else:
            print("Invalid input {}".format(raw_input))
        # if zombie.health > 0:
        #     zombie.attack(hero)

main()
