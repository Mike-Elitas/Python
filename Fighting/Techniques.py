class Technique:
    name = ""
    dmg = 0
    cd = 0

    def __init__(self, name, dmg, cd):
        self.name = name
        self.dmg = dmg
        self.cd = cd

    def viewTechnique(self):
        print ("La tecnica: " + self.name)
        print ("El dano: " + str(self.dmg))
        print ("El cooldown: " + str(self.cd))
        print (" ")
