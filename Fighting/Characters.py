from Fighting.Techniques import Technique

class Character:
    name = ""
    hp = 0
    maxHp = 0
    techniques = []

    def __init__(self, name, maxHp, techniques):
        self.name = name
        self.maxHp = maxHp
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

    def getTechniques(self):
        i = 1
        print("Habilidades:")
        for x in self.techniques:
            print(str(i) + ". " + Technique.getName(x))
            i = i+1
            Technique.viewTechnique(x)

    def viewCharacter(self):
        print(self.name + ":")
        print("HP: " + str(self.maxHp))
        print(" ")
        self.getTechniques()

    def fightTechniques(self):
        i = 1
        print("Habilidades:")
        for x in self.techniques:
            print(str(i) + ". " + Technique.getName(x) + "  DMG:" + str(Technique.getDmg(x)) + "  CD:" + str(Technique.getCurrentCd(x)))
            i = i + 1
        print("\n")