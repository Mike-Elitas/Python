from Fighting.Techniques import Technique
from Fighting.Characters import Character
import random

t1 = Technique("Auto Attack", 50, 1)
t4 = Technique("Auto Attack", 50, 1)
t2 = Technique("Hasaki", 80, 4)
t3 = Technique("Body Slam", 140, 6)
c1 = Character("El Moreno", 500, [t1, t2])
c2 = Character("Big Chungus", 700, [t4, t3])

characters = [c1, c2]

champlock = 0


def menu():
    menuInicio = input("------------------------------------------------ \n"
                       "Bienvenido a Soul Reaper V, entra a la batalla: \n"
                       "------------------------------------------------ \n"
                       "1. Jugar\n"
                       "2. Salir\n"
                       "------------------------------------------------ \n")
    if menuInicio == "1":
        champSelect()
    elif menuInicio == "2":
        exit()
    else:
        print("------------------------------------------------ \n"
              "Por favor escoja una opcion valida: \n"
              "------------------------------------------------")
        menu()


def display(champ):
    Character.viewCharacter(characters[champ - 1])
    currentChamp = (characters[champ - 1])
    lock(currentChamp)


def champSelect():
    print("----------------------------------------------")
    i = 1
    for x in characters:
        print(str(i) + ". " + x.getName())
        i = i + 1
    print("----------------------------------------------")
    champlock = int(input("Selecciona un personaje o pulsa '0' para salir al menu: "))
    if champlock == 0:
        menu()
    elif champlock == 1:
        display(champlock)

    elif champlock == 2:
        display(champlock)


def lock(currentChamp):
    lock = int(input("Pulsa 1 para fijar el personaje u otro numero para volver a la selccion: \n"))
    if lock == 1:
        player = currentChamp
        champIndex = characters.index(currentChamp)
        characters.remove(currentChamp)
        com = characters[random.randint(0, len(characters) - 1)]
        characters.insert(champIndex, currentChamp)
        startGame(player, com)
    else:
        champSelect()


def startGame(player, com):
    victory = False
    player.setHp(player.getMaxHp())
    com.setHp(com.getMaxHp())
    print(player.getName() + "            vs.            " + com.getName() + "\n")
    while not victory:
        print(str(player.getName()) + ": " + str(player.getHp()) + "HP                    " + str(
            com.getName()) + ": " + str(com.getHp()) + "HP\n")
        player.fightTechniques()
        print("0. Retirada")
        attack = int(input("Elije un ataque: \n"))
        if attack == 0:
            print("You Lose...")
            victory = True
        elif attack == 1:
            impact(attack, player, com)
        elif attack == 2:
            impact(attack, player, com)
        elif attack == 3:
            impact(attack, player, com)
        for x in player.techniques:
            if Technique.getCurrentCd(x) > 0:
                x.setCurrentCd(Technique.getCurrentCd(x)-1)
        for x in com.techniques:
            if Technique.getCurrentCd(x) > 0:
                x.setCurrentCd(Technique.getCurrentCd(x) - 1)
        if com.getHp() <= 0:
            print("You Win!")
            victory = True
            input("Presiona enter para volver al menu: ")
        elif player.getHp() <= 0:
            print("You Lose...")
            victory = True
            input("Presiona enter para volver al menu: ")
        else:
            print("----------------------------------------------\n")
    player.setHp(player.getMaxHp())
    com.setHp(com.getMaxHp())
    for x in player.techniques:
        x.setCurrentCd(0)
    for x in com.techniques:
        x.setCurrentCd(0)
    menu()


def impact(atk, fighter1, fighter2):

    if Technique.getCurrentCd(fighter1.techniques[atk-1]) > 0:
        print(fighter1.getName() + " descansa un turno porque esta habilidad esta en cooldown...\n")
    else:
        fighter2.setHp(fighter2.getHp() - Technique.getDmg(fighter1.techniques[atk-1]))
        Technique.setCurrentCd(fighter1.techniques[atk-1], Technique.getCd(fighter1.techniques[atk-1]))
        print(fighter1.getName() + " usa " + Technique.getName(fighter1.techniques[atk-1]) + "\n")
    rand = random.randint(0, len(fighter2.techniques)-1)
    if Technique.getCurrentCd(fighter2.techniques[rand]) > 0:
        print(fighter2.getName() + " descansa un turno porque esta habilidad esta en cooldown...\n")
    else:
        fighter1.setHp(fighter1.getHp() - Technique.getDmg(fighter2.techniques[rand]))
        Technique.setCurrentCd(fighter2.techniques[rand], Technique.getCd(fighter2.techniques[rand]))
        print(fighter2.getName() + " usa " + Technique.getName(fighter2.techniques[rand]) + "\n")
    input(rand)

menu()
