import random
import time

class Character:
    def __init__(self, health, power, name, coins, armor, evade):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins 
        self.armor = armor
        self.evade = evade
    def attack(self, enemy):
        if enemy.evade > 0:
            if random.randint(1, ((20/enemy.evade) + 1)) == 3:
                print(f"{enemy.name} has evaded the attack from {self.name}.")
        if enemy.evade > 0:
            if random.randint(1, ((20/enemy.evade) + 1)) == 3:
                print(f"{enemy.name} has evaded the attack from {self.name}.")
        else:
            self.damage = self.power - enemy.armor
            enemy.health -= self.damage
            print(f"{self.name} does {self.damage} damage to the {enemy.name}.\n")
        if enemy.health <= 0:
            print(f"{enemy.name} is dead.")
            print("""                                       
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@""")
            print(("The game is over"))
            quit()

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

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
    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)


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

class Orc(Character):
    pass

class Bard(Character):
    pass

class Dragon(Character):
    pass

class Tonic(object):
    cost = 5
    name = 'Tonic'
    def apply(self, hero):
        hero.health += 2
        print("{}'s health increased to {}.".format(hero.name, hero.health))

class SuperTonic(object):
    cost = 8
    name = 'Super Tonic'
    def apply(self, hero):
        hero.health += 10
        print("{}'s health increased to {}.".format(hero.name, hero.health))

class Sword(object):
    cost = 10
    name = 'Sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Armor(object):
    cost = 10
    name = 'Armor'
    def apply(self, hero):
        hero.armor += 2
        print("{}'s armor increased to {}.".format(hero.name, hero.armor))

class Evade(object):
    cost = 5
    name = 'Evade'
    def apply(self, hero):
        hero.evade += 2
        print("{}'s evade increased to {}.".format(hero.name, hero.evade))

class Hockey_stick(object):
    cost = 5
    name = 'Hockey Stick'
    def apply(self, hero):
        hero.power += 4
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Piggy_bank(object):
    cost = 5
    name = 'Piggy Bank'
    def apply(self, hero):
        hero.coins += 4
        print("{}'s coins increased to {}.".format(hero.name, hero.coins))

class Store():
    tonic = Tonic()
    super_tonic = SuperTonic()
    sword = Sword()
    armor = Armor()
    evade = Evade()
    hockey_stick = Hockey_stick()
    piggy_bank = Piggy_bank()
    items = [tonic, super_tonic, sword, armor, evade, hockey_stick, piggy_bank]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print(f"You have {hero.health} health, {hero.power} power, and {hero.coins} coins.")
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("8. Leave")
            raw_imp = int(input("> "))
            if raw_imp == 7:
                ItemToBuy = Store.items[raw_imp - 1]
                item = ItemToBuy
                hero.buy(item)
                break
            elif raw_imp == 8:
                break
            else:
                ItemToBuy = Store.items[raw_imp - 1]
                item = ItemToBuy
                hero.buy(item)
    def go_to_store(self, character):
        store_status = int(input("Press 1. to go to the store, Press 2. to journey on...."))
        if store_status == 1:
            self.do_shopping(character)
        else:
            exit

def main():

    hero = Hero(10, 5, "The Hero", 0, 0, 0)
    goblin = Goblin(6, 2, "The Goblin", 5, 0, 0)
    zombie = Zombie(1, 1, "The Zombie", 0, 0, 0)
    medic = Medic(5,1, "The Medic", 6, 0, 0 )
    shadow = Shadow(1, 1, "The Shadow", 10, 0, 0)
    orc = Orc(6,6,"The Orc", 15, 0, 0)
    bard = Bard(100, 1, "The Bard", 10, 0, 0)
    dragon = Dragon(8, 25, "The Dragon", 100, 0, 0)
    store = Store()
    print(f"\nIt's a showdown between the {goblin.name} and {hero.name}!\n")
    while goblin.alive() and hero.alive():
        print("-" * 40)
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight the goblin.")
        print("2. Do nothing.")
        print("3. Flee the fight.")
        print("*" * 40)
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
    print()
    print(f"Would you like to go to the store? ")
    print()
    store.go_to_store(hero)
    print()
    
    print("*" * 40)
    print(f"A new enemy is approaching... ")
    print(f"\nIt's a showdown between the {zombie.name} and {hero.name}!\n")
    while zombie.alive() and hero.alive():
        print("-" * 40)
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
    print()
    print(f"Would you like to go to the store? ")
    print()
    store.go_to_store(hero)
    print()
    
    print("*" * 40)
    print(f"A new enemy is approaching... ")
    print(f"\nIt's a showdown between the {medic.name} and {hero.name}!\n")
    while medic.alive() and hero.alive():
        print("-" * 40)
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
    print()
    print(f"Would you like to go to the store? ")
    print()
    store.go_to_store(hero)
    print()
    
    print("*" * 40)
    print(f"A new enemy is approaching... ")
    print(f"\nIt's a showdown between the {shadow.name} and {hero.name}!\n")
    while shadow.alive() and hero.alive():
        print("-" * 40)
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
    print()
    print(f"Would you like to go to the store? ")
    print()
    store.go_to_store(hero)
    print()
    
    print("*" * 40)
    print(f"A new enemy is approaching... ")  
    print(f"\nIt's a showdown between the {orc.name} and {hero.name}!\n")
    while orc.alive() and hero.alive():
        print("-" * 40)
        hero.print_status()
        orc.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight the orc.")
        print("2. Do nothing.")
        print("3. Flee the fight.")
        print("*" * 40)
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(orc)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if orc.health > 0:
            orc.attack(hero)
    print()
    print()
    print(f"Would you like to go to the store? ")
    print()
    store.go_to_store(hero)
    print()
    
    print("*" * 40)
    print(f"A new enemy is approaching... ")  
    print(f"\nIt's a showdown between the {bard.name} and {hero.name}!\n")
    while bard.alive() and hero.alive():
        print("-" * 40)
        hero.print_status()
        bard.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight the bard.")
        print("2. Do nothing.")
        print("3. Flee the fight.")
        print("*" * 40)
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            print("How dare you! BE GONE....")
            break
        elif raw_input == "2":
            print("Your benevolence has served you well... BE HEALED.")
            hero.health += 5
            break
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
    print()
    print()
    print(f"Would you like to go to the store? ")
    print()
    store.go_to_store(hero)
    print()
    
    print("*" * 40)
    print(f"It's the final battle... ")
    print(f"\nIt's a showdown between the {dragon.name} and {hero.name}!\n")
    while dragon.alive() and hero.alive():
        print("-" * 40)
        hero.print_status()
        dragon.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight the dragon.")
        print("2. Do nothing.")
        print("3. Flee the fight.")
        print("*" * 40)
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(dragon)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if dragon.health > 0:
            dragon.attack(hero)
    print()
    print("YOU SLAYED THE DRAGON! YOU WIN!!!!!!")


main()























