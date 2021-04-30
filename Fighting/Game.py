from Fighting.Techniques import Technique
from Fighting.Characters import Character

t1 = Technique("Auto Attack", 50, 1)
t2 = Technique("Hasaki", 80, 4)
t3 = Technique("Body Slam", 140, 6)
c1 = Character("El Moreno", 500, [t1, t2])
c2 = Character("Big Chungus", 700, [t1, t3])

characters = [c1, c2]


def menu():

    menuInicio = input("------------------------------------------------ \n"
        "Bienvenido a Soul Reaper V, entra a la batalla: \n"
        "------------------------------------------------ \n"
        "1. Jugar\n"
        "2. Salir\n"
        "------------------------------------------------ \n")
    if menuInicio == 1:
        champSelect()
    elif menuInicio == 2:
        exit()
    else:
        print("------------------------------------------------ \n"
              "Por favor escoja una opcion valida: \n"
              "------------------------------------------------")
        menu()

def champSelect():
    print ("----------------------------------------------")
    i = 1
    for x in characters:
        print (str(i) + ". " + x.getName())
        i = i + 1
    print ("----------------------------------------------")
    champ = input("Selecciona un personaje o pulsa '0' para salir al menu: ")
    if champ == 0:
        menu()
    elif champ == 1:
        Character.viewCharacter(characters[champ-1])
    # Character.viewCharacter(c1)
    # lock = input("Pulsa 1 para fijar el personaje u otra tecla para volver a la selccion: ")
    # if lock == 1:
    #     startGame

menu()


# def startGame():
#     # while c1.hp != 0 & c2.hp != 0:
