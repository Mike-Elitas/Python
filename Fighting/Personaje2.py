from TecnicaP2 import TecnicaP2

class Personaje2:

    nombre = "Dr. Radiactivo"
    vida = 350
    descripcion = "El Dr. Garcia era un doctor de un hospital especializado en la cura del cancer, que, como muchos otros se dedicaba a " "\n" \
                  "la investigacion de la cura, pero lo suyo era personal, habia perdido dos personas cercanas. Por culpa de esa enfermedad," "\n" \
                  "se quedaba horas extras en el laboratorio haciendo pruebas, relizando mezclas... Un dia el doctor se empezo a encontrar mal, " "\n" \
                  "a las semana le diagnosticaron esa enfermedad que tanto males le habia creado. Tenia un supuesto remedio no probado por ningun" "\n" \
                  "ser vivo, era una mezcla de muchos quimicos que por separado reducian los efectos de la enfermedad, el decidio juntarlos y probarlos con " "\n" \
                  "si mismo. Cayo en coma del cual desperto a los meses, ya curado y con unas habilidades no humanas..."

    golpes = []

    def __init__(self):

        self.golpes.append(TecnicaP2)

    def mostrar(self):

        print("Nombre: " + self.nombre + "\n"
              "Vida: " + str(self.vida) + "\n"
              "Historia: " + self.descripcion)

    def restvida(self, vidat):

        vida = vida - vidat

    #def ataque(self, P1):



    #def esquivar(self):

    def mostrarAtaques(self):

        print(TecnicaP2.golpe1(self) ,
              TecnicaP2.golpe2(self) ,
              TecnicaP2.golpe3(self))