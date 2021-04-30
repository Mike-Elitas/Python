class TecnicaP1:

    nombre = ""
    vidat = 0
    tipo = ""

    def golpe1(self):

        self.nombre = "Bomba Infierno"
        self.tipo = "Especial"
        self.vidat = 15

        print(" \n"
            "-------------------------------------\n"
            "Ataque 1 " + self.nombre + "\n" \
              "Tipo " + self.tipo + "\n" \
              "Dano " + str(self.vidat) + "\n" \
              "-----------------------------------")

    def golpe2(self):

        self.nombre = "Patada Giro Ignea"
        self.tipo = "Fisico y Especial"
        self.vidat = 35

        print("Ataque 2 " + self.nombre + "\n" \
              "Tipo " + self.tipo + "\n" \
              "Dano " + str(self.vidat) + "\n" \
              "-----------------------------------")

    def golpe3(self):

        self.nombre = "Llamarada Tsunami"
        self.tipo = "Fuego"
        self.vidat = 60

        print("Ataque 3: " + self.nombre + "\n" \
              "Tipo: " + self.tipo + "\n" \
              "Dano: " + str(self.vidat) + "\n" \
              "-----------------------------------\n")