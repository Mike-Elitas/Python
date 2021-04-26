from Fighting.Techniques import Technique

class Character:
    name = ""
    hp = 0
    techniques = []

    def __init__(self, name, hp, techniques):
        self.name = name
        self.hp = hp
        self.techniques = techniques

    def getName(self):
        print (self.name)

    def getHp(self):
        print (self.hp)

    def getTechniques(self):
        for x in self.techniques:
            Technique.viewTechnique(x)

    def viewCharacter(self):
        print ("El personaje: " + self.name)
        print ("La vida: " + str(self.hp))
        print (" ")
        self.getTechniques()
