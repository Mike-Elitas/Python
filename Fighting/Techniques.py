class Technique:
    name = ""
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

    def __init__(self, name, dmg, cd):
        self.name = name
        self.dmg = dmg
        self.cd = cd

    def viewTechnique(self):
        print("Tecnica: " + self.getName())
        print("DMG: " + str(self.getDmg()))
        print("Cooldown: " + str(self.getCd()))
        print(" ")
