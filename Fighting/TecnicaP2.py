class TecnicaP2:
    nombre = ""
    vidat = 0
    tipo = ""

    def golpe1(self):
        self.nombre = "Somnolencia"
        self.tipo = "Psiquico"
        self.vidat = 10

        print(" \n"
            "-------------------------------------\n"
            "Ataque 1 " + self.nombre + "\n" \
              "Tipo " + self.tipo + "\n" \
              "Dano " + str(self.vidat) + "\n" \
              "-----------------------------------")

    def golpe2(self):
        self.nombre = "Bomba acida "
        self.tipo = "Quimico"
        self.vidat =30

        print("Ataque 2 " + self.nombre + "\n" \
              "Tipo " + self.tipo + "\n" \
              "Dano " + str(self.vidat) + "\n" \
              "-----------------------------------")

    def golpe3(self):
        self.nombre = "Rayos Radioactivos"
        self.tipo = "Quimico"
        self.vidat = 65

        print("Ataque 3: " + self.nombre + "\n" \
              "Tipo: " + self.tipo + "\n" \
              "Dano: " + str(self.vidat) + "\n" \
              "-----------------------------------\n")