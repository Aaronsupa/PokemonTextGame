import requests


def instructions():
    print("Welcome to PokePlay!")
    print("In this game you'll choose your new digital companion and train it to be the strongest pokemon ever!")
    answer = input("Are you up to the challenge? (y/n): ")
    if(answer.lower() == "y"):
        return True
    return False

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

def runGame():
    userAnswer = instructions()
    if(userAnswer):
        myPokemonData = getUserPokemon()
        myName = pokeName()
        mySpecies = myPokemonData.json()["name"]
        print("Your", mySpecies, "is now named", myName)
    else:
        print("That's too bad... see you next time!")

runGame()