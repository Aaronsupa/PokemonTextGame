import requests


def instructions():
    print("Welcome to PokePlay!")
    print("In this game you'll choose your new digital companion and train it to be the strongest pokemon ever!")
    answer = input("Are you up to the challenge? (y/n): ")
    if(answer.lower() == "y"):
        return True
    return False

def options():
    print("What would you like to do now? Type the number of the corresponding choice")
    print("1: Train Pokemon")
    print("2: Battle a Random Pokemon")
    print("3: Feed my Pokemon")
    print("4: See my Pokemon's stats")
    answer = int(input())
    while(answer > 4 or answer < 0):
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
    print("Name:", userPokemon.name)
    print("Species:", data["name"])
    print("Height:", data['height'])
    print("Weight:", data['weight'])
    print("Health:", userPokemon.health)
    length = len(data["abilities"])
    for ability in range(length):
        print("Abilities:", data["abilities"][ability]["ability"]["name"])

def feedPokemon(userPokemon):
    if(userPokemon.health == 100):
        print("No need to eat!")
    else: 
        userPokemon.eat()
        print("Health updated!")

def trainPokemon(userPokemon):
    if userPokemon.health <= 20:
        print("Health is too low to train!")
    else:
        userPokemon.train()

def runGame():
    userAnswer = instructions()
    if(userAnswer):
        myPokemon = getUserPokemon()
        myPokemonData = myPokemon.json()
        myName = pokeName()
        userPokemon = pokemon(myName, 100)
        mySpecies = myPokemonData["name"]
        print("Your", mySpecies, "is now named", myName)
        keepPlaying = True
        while(keepPlaying):
            opt = options()
            if(opt == 4):
                pokeStats(myPokemonData, userPokemon)
            elif(opt == 3):
                feedPokemon(userPokemon)
            elif(opt == 1):
                trainPokemon(userPokemon)
            

    else:
        print("That's too bad... see you next time!")

class pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = 100

    def setName(self, name):
        self.name = name 

    def eat(self, health):
        if(health > 90):
            self.health = 100
        else:
            self.health += 10

    def train(self, health):
        self.health -= 20


runGame()