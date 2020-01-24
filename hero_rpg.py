import random
import time

class Character:
    def __init__(self, health, power, name, coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins 
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

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))


class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Store(object):
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            raw_imp = int(input("> "))
            if raw_imp == 10:
                break
            else:
                ItemToBuy = Store.items[raw_imp - 1]
                item = ItemToBuy()
                hero.buy(item)
    def go_to_store(self, character):
        store_status = int(input("Press 1. to go to the store, Press something else to journey on...."))
        if store_status == 1:
            self.do_shopping(character)

class Hero(Character):  
    def crit_chance(self):
        self.critical_strike = 1
        if random.randint(1,6) == 1:
            self.critical_strike = 2
            print(f"{self.name} lands a critical strike!")
        return self.critical_strike
    def attack(self, enemy):
        self.damage = self.power * self.crit_chance()
        enemy.health -= self.damage
        print(f"{self.name} does {self.damage} to {enemy.name}!")
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!") 
            self.coins += enemy.coins
            print(f"You gained {enemy.coins} coins. You now have {self.coins} coins.")


class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        return True

class Medic(Character):
    def crit_heal_chance(self):
        if random.randint(1,6) == 1:
            self.health += 2
            print(f"Oh no, {self.name} is healing! They regenerated two HP!")

class Shadow(Character):
    pass

def main():

    hero = Hero(100, 5, "Rand al'Thor", 0)
    goblin = Goblin(6, 2, "The Goblin", 5)
    zombie = Zombie(1, 1, "The Zombie", 100)
    medic = Medic(5,1, "The Medic", 6 )
    shadow = Shadow(1, 1, "The Shadow", 10)
    store = Store()

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
Good job defeating the {goblin.name}, {hero.name}! 
    """)
    print("*" * 40)
    store.go_to_store(hero)
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
            print("But what is dead doesn't always die.....")
            zombie.attack(hero)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Smart move! They can't die you know.....")
            break
        else:
            print("Invalid input {}".format(raw_input))
    print()
    print("*" * 40)
    store.go_to_store(hero)
    print("*" * 40)
    print(f"""
A new enemy is approaching.....
    """)
    print("*" * 40)
    print()
    while medic.alive() and hero.alive():
        hero.print_status()
        medic.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight the medic.")
        print("2. Do nothing.")
        print("3. Flee the fight.")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(medic)
            medic.crit_heal_chance()
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if medic.health > 0:
            medic.attack(hero)
    print()
    print("*" * 40)
    store.go_to_store(hero)
    print(f"""
Good job defeating the {medic.name}, {hero.name}! A new enemy is approaching.....
    """)
    print("*" * 40)
    while shadow.alive() and hero.alive():
        hero.print_status()
        shadow.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight the shadow.")
        print("2. Do nothing.")
        print("3. Flee the fight.")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            if random.randint(1,11) == 1 :
                print(f"{shadow.name} defense's are down! You can strike...")
                hero.attack(shadow)
            else:
                print("Shadow dodges the attack!")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if shadow.health > 0:
            shadow.attack(hero)
    print()
    print("*" * 40)
    store.go_to_store(hero)
    print(f"""
Good job defeating the {shadow.name}, {hero.name}! A new enemy is approaching.....
    """)
    print("*" * 40)
    print()    
main()























