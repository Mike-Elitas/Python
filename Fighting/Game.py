from Fighting.Techniques import Technique
from Fighting.Characters import Character

t1 = Technique("Auto Atack", 50, 1)
t2 = Technique("Hasaki", 80, 4)
t3 = Technique("Body Slam", 140, 6)
c1 = Character("Yasuo", 500, [t1, t2])
c2 = Character("Big Chungus", 700, [t1, t3])

characters = [c1, c2]


def displayCharacter(characters):
    Character.viewCharacter()
    lock = input("Pulsa 1 para fijar el personaje u otra tecla para volver a la selccion: ")
    # if lock == 1:
    #     startGame

    i = 0
    for x in characters:
        print (str(i) + ". " + x.name)
        i = i+1


# def startGame():
#     # while c1.hp != 0 & c2.hp != 0:
c1.getTechniques()

