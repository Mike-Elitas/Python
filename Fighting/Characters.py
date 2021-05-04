from Techniques import Technique

class Character:
    # Inicializacion de variables
    name = ""
    hp = 0
    descripcion = ""
    maxHp = 0
    techniques = []
    # Constructor necesario para crear los personajes en el juego
    def __init__(self, name, maxHp, descripcion, techniques):
        self.name = name
        self.maxHp = maxHp
        self.descripcion = descripcion
        self.techniques = techniques

    def getName(self):
        return(self.name)

    def setName(self, name):
        self.name = name

    def getMaxHp(self):
        return self.maxHp

    def getHp(self):
        return(self.hp)

    def setHp(self, hp):
        self.hp = hp
    # Visualizador de tecnicas del personaje, usado en el visualizador de usuario
    def getTechniques(self):
        i = 1
        print("---------------------------")
        print("Habilidades:")
        print("---------------------------")
        for x in self.techniques:
            print(str(i) + ". " + Technique.getName(x))
            i = i+1
            Technique.viewTechnique(x)
    # Visualizador de la informacion de usuario, usado en el meni
    def viewCharacter(self):
        print(self.name + ":")
        print("HP: " + str(self.maxHp))
        print("Historia: " + self.descripcion)
        print(" ")
        self.getTechniques()
    # Visualizador de tecnicas con el formato de combate
    def fightTechniques(self):
        i = 1
        print("---------------------------")
        print("Habilidades:")
        print("---------------------------")
        for x in self.techniques:
            print(str(i) + ". " + Technique.getName(x) + "  DMG:" + str(Technique.getDmg(x)) + "  CD:" + str(Technique.getCurrentCd(x)))
            print("-------------------------------------")
            i = i + 1
