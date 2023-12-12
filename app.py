import requests
import random


def instructions():
    print("Welcome to PokePlay!")
    print("In this game you'll choose your new digital companion and train it to be the strongest pokemon ever!")
    answer = input("Are you up to the challenge? (y/n): ")
    if(answer.lower() == "y"):
        return True
    return False

def options():
    print("What would you like to do now? Type the number of the corresponding choice")
    print("[1] Train Pokemon")
    print("[2] Battle a Random Pokemon")
    print("[3] Feed my Pokemon")
    print("[4] See my Pokemon's stats")
    answer = int(input("Your Choice: "))
    while(answer > 4 or answer <= 0):
          answer = int(input("Invalid answer: "))
    return answer

def getUserPokemon():
    poke = input("Choose your pokemon: ").lower()
    respond = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(poke))
    while(respond.status_code != 200):
        poke = input("Choose your pokemon: ").lower()
        respond = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(poke))
    return respond

def pokeName():
    name = input("Choose a name for your Pokemon: ")
    return name

def pokeStats(data, userPokemon):
    print("\n")
    print("Name:", userPokemon.name)
    print("Species:", data["name"])
    print("Level: ", userPokemon.level)
    print("Height:", data['height'])
    print("Weight:", data['weight'])
    print("Health:", userPokemon.health)
    length = len(data["abilities"])
    for ability in range(length):
        print("Abilities:", data["abilities"][ability]["ability"]["name"])
    print("\n")

def feedPokemon(userPokemon):
    print("\n")
    if(userPokemon.health == 100):
        print("No need to eat!")
    else: 
        userPokemon.eat()
        print("Health updated!")
        print("Current health:", userPokemon.health)
    print("\n")
    

def trainPokemon(userPokemon):
    print("\n")
    if(userPokemon.health <= 20):
        print("Health is too low to train!")
    else:
        if(userPokemon.level < 100):
            userPokemon.train()
        else:
            print("Max Level Reached!")
    print("Current level:", userPokemon.level)
    print("Current health:", userPokemon.health)
    print("\n")

def battlePokemon(userPokemon):
    print("\n")
    rand = random.randint(0,100 - userPokemon.level)
    userPokemon.health -= rand
    if(userPokemon.health <= 0):
        print("You Died!", end = "\n")
        print("See you next time!")
        return False
    print(userPokemon.name, "survived the battle.", end = "\n")
    gainLevel = random.randint(0,1)
    if(gainLevel == 1):
        userPokemon.level+=1
        print("You gained a level!")
    print("Current health:", userPokemon.health)
    print("\n")
    return True

def runGame():
    userAnswer = instructions()
    if(userAnswer):
        myPokemon = getUserPokemon()
        myPokemonData = myPokemon.json()
        myName = pokeName()
        userPokemon = pokemon(myName)
        mySpecies = myPokemonData["name"]
        print("Your", mySpecies, "is now named", myName)
        keepPlaying = True
        while(keepPlaying):
            opt = options()
            if(opt == 4):
                pokeStats(myPokemonData, userPokemon)
            elif(opt == 3):
                feedPokemon(userPokemon)
            elif(opt == 2):
                result = battlePokemon(userPokemon)
                if(not result):
                    break
            elif(opt == 1):
                trainPokemon(userPokemon)
            keepPlaying = keepPlayingGame()
    else:
        print("That's too bad... see you next time!")

def keepPlayingGame():
    userAnswer = input("Would you like to keep playing? (y/n):")
    if(userAnswer.lower() == "y"):
        return True
    else:
        print("Too bad... See you next time!")
        return False


class pokemon:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 0

    def setName(self, name):
        self.name = name 

    def eat(self):
        if(self.health > 90):
            self.health = 100
        else:
            self.health += 10

    def train(self):
        self.health -= 20
        self.level += 1


runGame()