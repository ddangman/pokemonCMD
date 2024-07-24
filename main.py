# https://www.youtube.com/watch?v=Pbs6jQZrZA4

import time
import numpy as np
import sys

# define a Pokemon object
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='===================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # amount of health bars

# delay printing to the console
# https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def print_active_pokemon(Pokemon):
    print(f"\n{Pokemon.name}")
    print("TYPE/", Pokemon.types)
    print("ATTACK/", Pokemon.attack)
    print("DEFENSE/", Pokemon.defense)
    # level is not defined in the __init__ method,
    # level is defined by this expression
    print("LVL/", 3*(1+np.mean([Pokemon.attack, Pokemon.defense])))

def pokemon_turn(Pokemon1, Pokemon2, attack_string):
    print(f"Go {Pokemon1.name}!")
    for i, x in enumerate(Pokemon1.moves):
        print(f"{i+1}.", x)
    index = int(input('Pick a move: '))
    delay_print(f"\n{Pokemon1.name} used {Pokemon1.moves[index-1]}!")
    time.sleep(1)

    delay_print(attack_string)
    # determine damage
    Pokemon2.bars -= Pokemon1.attack

    # redraw health bars by first clearing the screen, then printing the health bars
    Pokemon2.health = "" # clear health bars
    # calculate health bars with defense boost
    for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)): 
        Pokemon2.health += "=" # concatenate health bars
    time.sleep(1)
    # show updated health bars
    print(f"\n{Pokemon1.name}\t\tHEALTH\t{Pokemon1.health}")
    print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
    time.sleep(.5)

def fight(Pokemon1, Pokemon2):
    # allow two Pokemon to fight each other

    # print fight information
    print("-----POKEMON BATTLE-----")
    print_active_pokemon(Pokemon1)
    print("\nVS")
    print_active_pokemon(Pokemon2)

    # pause game to see the fight information
    time.sleep(2)

    # consider type advantages similar to Rock, Paper, Scissors
    version = ['Fire', 'Water', 'Grass']
    for index, value in enumerate(version):
        # player's active pokemon type
        if Pokemon1.types == value:
            # enemy's active pokemon type is the same
            if Pokemon2.types == value:
                string_1_attack = '\nStandard effectiveness...'
                string_2_attack = '\nStandard effectiveness...'
            # enemy's active pokemon type is stronger
            if Pokemon2.types == version[(index+1)%3]:
                Pokemon2.attack *= 2
                Pokemon1.attack /= 2
                string_1_attack = '\nIts not very effective...'
                string_2_attack = '\nIts super effective!'
            # enemy's active pokemon type is weaker
            if Pokemon2.types == version[(index+2)%3]:
                Pokemon1.attack *= 2
                Pokemon2.attack /= 2
                string_1_attack = '\nIts super effective!'
                string_2_attack = '\nIts not very effective!'

    # battle logic loop
    # Continue while pokemon still have health
    while (Pokemon1.bars > 0) and (Pokemon2.bars > 0):
        # print the health of each pokemon
        print(f"\n{Pokemon1.name}\t\tHEALTH\t{Pokemon1.health}")
        print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")

        # Pokemon1's turn
        pokemon_turn(Pokemon1, Pokemon2, string_1_attack)
        # check if Pokemon2 fainted
        if Pokemon2.bars <= 0:
            delay_print("\n..." + Pokemon2.name + ' fainted.')
            break

        # Pokemon2's turn
        pokemon_turn(Pokemon2, Pokemon1, string_2_attack)
        # check if Pokemon2 fainted
        if Pokemon1.bars <= 0:
            delay_print("\n..." + Pokemon1.name + ' fainted.')
            break

    money = np.random.choice([100, 200, 300, 400, 500])
    delay_print(f"\nOpponent paid you ${money}.\n")





if __name__ == '__main__':
    # create Pokemon
    Charizard = Pokemon ('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8}) 
    Blastoise = Pokemon ('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10}) 
    Venusaur = Pokemon ('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {'ATTACK':8, 'DEFENSE':12})

    Charmeleon = Pokemon ('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'], {'ATTACK':6, 'DEFENSE':5}) 
    Wartortle = Pokemon ('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'], {'ATTACK': 5, 'DEFENSE':5}) 
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'], {'ATTACK':4, 'DEFENSE':6})

    Charmander = Pokemon ('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], {'ATTACK':4, 'DEFENSE':2}) 
    Squirtle = Pokemon ('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'ATTACK': 3, 'DEFENSE':3}) 
    Bulbasaur = Pokemon ('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'], {'ATTACK':2, 'DEFENSE':4})

    # fight
    fight(Charizard, Wartortle)
