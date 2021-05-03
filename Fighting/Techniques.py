class Technique:
    # Inicialización de variables
    name = ""
    tipo = ""
    dmg = 0
    cd = 0
    currentCd = 0

    def getName(self):
        return self.name

    def getDmg(self):
        return self.dmg

    def getCd(self):
        return self.cd

    def getCurrentCd(self):
        return self.currentCd

    def setCurrentCd(self, currentCd):
            self.currentCd = currentCd
    # Constructor necesario para usar las tecnicas en el juego
    def __init__(self, name, tipo, dmg, cd):
        self.name = name
        self.tipo = name
        self.dmg = dmg
        self.cd = cd
    # Visualiza la informacion de la tecnica con formato
    def viewTechnique(self):
        print("Tecnica: " + self.getName())
        print("Tipo: " + self.tipo)
        print("DMG: " + str(self.getDmg()))
        print("Cooldown: " + str(self.getCd()))
        print("---------------------------")