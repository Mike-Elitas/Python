from Techniques import Technique
from Characters import Character
import random
# Instanciacion de tecnicas y personajes
t1 = Technique("Mordida", "Fisico", 50, 1)

t2 = Technique("Patadas", "Fisico", 80, 4)

t3 = Technique("Body Slam", "Fisico", 140, 6)

t4 = Technique("Bomba Infierno", "Especial", 40, 1)

t5 = Technique("Patada Giro Ignea", "Fisico / Especial",  65, 2)

t6 = Technique("Llamarada Tsunami", "Fuego", 100, 5)

t7 = Technique("Radiolaser", "Quimico", 55, 1)

t8 = Technique("Bomba acida", "Quimico", 75, 4)

t9 = Technique("Rayos Radioactivos", "Quimico", 150, 6)

t10 = Technique("Mataleon", "Fisico", 50, 1)

t11 = Technique("Arrojadizo", "Arma", 65, 2)

t12 = Technique("Disparo Certero", "Arma", 120, 5)

c1 = Character("Sargento", 550, "Era un soldado del ejercito de Estados Unidos al que le toco luchar por su patria en Iran, lo capturaron los enemigos \n"
                    "lo torturaron para sacar informacion sobre las estrategias, armas, numero de hombres que llevaba su ejercito pero el no dijo nada \n"
                    "asi que le siguieron torturando hasta que un dia, al limite de la muerte, su cuerpo empezo a desarrollar una resistencia, fueza y punteria \n"
                    "sobrehumana a los golpes, cortes, ahogamientos, privaciones del descanso y en el momento en el que le dejaron solo se desato y salio \n"
                    "matando a los hombres que vigilaban la puerta con sus propias manos y con la ayuda de un arma consiguio escapar de la lineas enemigas. \n", [t10, t11, t12])

c2 = Character("Big Chungus", 700, "Big Chungus, antes conocido como Bugs Bunny, le despidieron de su trabajo y a raiz de eso se abandono y se dio a la comida basura, \n"
                      "la vida sedentaria, entonces engordo, pero eso no era ningun obstaculo para meterse en peleas ya que por su peso tenia mucha fuerza.",  [t1, t2, t3])

c3 = Character("Magma", 500, "Magma era una chica de 15 llamada Carolina, a esa edad su casa se incencdio y sus padres murieron ella al ver que se iba a quedar sola \n"
                  "no se molesto en salir de aquella casa en llamas, quiso morir con lo que mas queria, sus padres. Quedo inconsciente por el humo y lo que \n"
                  "ella penso que era el final, acabo siendo el principio de una larga y compleja historia, desperto a los dos dias en el hospital de su ciudad \n"
                  "sin a penas una quemadura, los medicos no se lo creian. Lo que Carolina iba a descubrir mas tarde es que aquel dia en el incendio absorbio \n"
                  "todas las llamas que tocaron su cuerpo y obtuvo los superpoderes de fuego que a dia de hoy usa contra sus rivales.", [t4, t5, t6])

c4 = Character("Dr. Radiactivo", 650, "El Dr. Garcia era un doctor de un hospital especializado en la cura del cancer, que, como muchos otros se dedicaba a \n"
                  "la investigacion de la cura, pero lo suyo era personal, habia perdido dos personas cercanas. Por culpa de esa enfermedad, \n"
                  "se quedaba horas extras en el laboratorio haciendo pruebas, relizando mezclas... Un dia el doctor se empezo a encontrar mal, \n"
                  "a las semana le diagnosticaron esa enfermedad que tanto males le habia creado. Tenia un supuesto remedio no probado por ningun \n"
                  "ser vivo, era una mezcla de muchos quimicos que por separado reducian los efectos de la enfermedad, el decidio juntarlos y probarlos con \n"
                  "si mismo. Cayo en coma del cual desperto a los meses, ya curado y con unas habilidades no humanas...", [t7, t8, t9] )

# Guardamos los personajes en un array para acceder facilmente
characters = [c1, c2, c3, c4]


def menu():
    # Menu de inicio
    menuInicio = int(input("------------------------------------------------ \n"
                       "Bienvenido a Soul Reaper V, entra a la batalla: \n"
                       "------------------------------------------------ \n"
                       "1. Jugar\n"
                       "2. Salir\n"
                       "------------------------------------------------ \n"))
    if menuInicio == 1:
        champSelect()
    elif menuInicio == 2:
        exit()
    else:
        # Si se introduce un valor incorrecto redirige al menu inicial
        print("------------------------------------------------ \n"
              "Por favor escoja una opcion valida: \n"
              "------------------------------------------------")
        menu()


def display(champ):
    # Muestra la informacion de los personajes en la pantalla de seleccion
    Character.viewCharacter(characters[champ - 1])
    currentChamp = (characters[champ - 1])
    lock(currentChamp)


def champSelect():
    # Muestra los personajes seleccionables para el combate
    print("----------------------------------------------")
    i = 1
    for x in characters:
        # Bucle para mostrarlos ordenados
        print(str(i) + ". " + x.getName())
        i = i + 1
    print("---------------------------------------------- \n")
    champlock = int(input("Selecciona un personaje o pulsa '0' para salir al menu: \n"))
    if champlock == 0:
        menu()
    elif champlock == 1:
        display(champlock)

    elif champlock == 2:
        display(champlock)

    elif champlock == 3:
        display(champlock)

    elif champlock == 4:
        display(champlock)

    else:
        # Si se introduce un valor incorrecto redirige al menu inicial
        print("------------------------------------------------ \n"
              "Por favor escoja una opcion valida: \n"
              "------------------------------------------------")
        menu()



def lock(currentChamp):
    lock = int(input("\n---------------------------------------------------------------------------------"
        "\nPulsa 1 para fijar el personaje u otro numero para volver a la selccion: \n"
                     "--------------------------------------------------------------------------------- \n"))
    if lock == 1:
        # Fija el personaje del usuario y genera un rival aleatorio de entre los demas
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
    # Inicia la vida de los personajes al comienzo de la batalla, empiezan en cero para conservar la vida original en otra variable
    player.setHp(player.getMaxHp())
    com.setHp(com.getMaxHp())
    print("======================================================")
    print(player.getName() + "                vs.             " + com.getName())
    print("====================================================== \n")
    while not victory:
        # Bucle funcional del juego. En caso de empate gana por defecto el usuario!
        print("====================== Vida ==========================")
        print(str(player.getName()) + ": " + str(player.getHp()) + "HP                   " + str(
            com.getName()) + ": " + str(com.getHp()) + "HP")
        print("====================================================== \n")
        player.fightTechniques()
        print("0. Retirada")
        print("------------------------------------- \n")
        print("================")
        attack = int(input("Elije un ataque: \n"
                           "================ \n"))
        if attack == 0:
            # Opcion adicional para salir del combate instantaneamente
            print("======================")
            print("You Lose...")
            print("A tu casa!! Cagaaao!!!")
            print("======================\n")
            victory = True
        # Selector de ataques
        elif attack == 1:
            impact(attack, player, com)
        elif attack == 2:
            impact(attack, player, com)
        elif attack == 3:
            impact(attack, player, com)
        # Bucles que actualizan el cooldown de todas la habilidades
        for x in player.techniques:
            if Technique.getCurrentCd(x) > 0:
                x.setCurrentCd(Technique.getCurrentCd(x)-1)
        for x in com.techniques:
            if Technique.getCurrentCd(x) > 0:
                x.setCurrentCd(Technique.getCurrentCd(x) - 1)
        # Condiciones de victoria y derrota
        if com.getHp() <= 0:
            print("=================")
            print("You Win!")
            print("Eres un campeon!!")
            print("=================\n")
            victory = True
            input("Presiona enter para volver al menu: \n")
        elif player.getHp() <= 0:
            print("====================================")
            print("You Lose...")
            print("Ni que esto fuera Dark Souls... :(")
            print("====================================\n")
            victory = True
            input("Presiona enter para volver al menu: ")
        else:
            print("----------------------------------------------\n")
    # Restauracion de vida y cooldown para volver a jugar sin reinicios
    player.setHp(player.getMaxHp())
    com.setHp(com.getMaxHp())
    for x in player.techniques:
        x.setCurrentCd(0)
    for x in com.techniques:
        x.setCurrentCd(0)
    menu()


def impact(atk, fighter1, fighter2):
    # Comprobacion de que la habilidad usada no este en Cooldown/Mensajes y calculos de dano player
    if Technique.getCurrentCd(fighter1.techniques[atk-1]) > 0:
        print( "\n" +  fighter1.getName() + " descansa un turno porque esta habilidad esta en cooldown...\n")
    else:
        fighter2.setHp(fighter2.getHp() - Technique.getDmg(fighter1.techniques[atk-1]))
        Technique.setCurrentCd(fighter1.techniques[atk-1], Technique.getCd(fighter1.techniques[atk-1]))
        print("\n" "-------------------------------- \n" + fighter1.getName() + " usa " + Technique.getName(fighter1.techniques[atk-1]) + "\n")
    # Comprobacion de que la habilidad usada no este en Cooldown/Mensajes y calculos de dano com + generacion de ataque aleatorio
    rand = random.randint(0, len(fighter2.techniques)-1)
    if Technique.getCurrentCd(fighter2.techniques[rand]) > 0:
        print(fighter2.getName() + " descansa un turno porque esta habilidad esta en cooldown...\n")
    else:
        fighter1.setHp(fighter1.getHp() - Technique.getDmg(fighter2.techniques[rand]))
        Technique.setCurrentCd(fighter2.techniques[rand], Technique.getCd(fighter2.techniques[rand]))
        print(fighter2.getName() + " usa " + Technique.getName(fighter2.techniques[rand]) + "\n" "-------------------------------- \n")
    input("Pulsa Enter para continuar. \n")
# Inicializacion del menu del juego
menu()
