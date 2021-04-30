from TecnicaP1 import TecnicaP1

class Personaje1:

    nombre = "Magma"
    vida = 300
    descripcion = "Magma era una chica de 15 llamada Carolina, a esa edad su casa se incencdio y sus padres murieron ella al ver que se iba a quedar sola \n" \
                   "no se molesto en salir de aquella casa en llamas, quiso morir con lo que mas queria, sus padres. Quedo inconsciente por el humo y lo que \n" \
                  "ella penso que era el final, acabo siendo el principio de una larga y compleja historia, desperto a los dos dias en el hospital de su ciudad \n" \
                  "sin a penas una quemadura, los medicos no se lo creian. Lo que Carolina iba a descubrir mas tarde es que aquel dia en el incendio absorbio \n" \
                  "todas las llamas que tocaron su cuerpo y obtuvo los superpoderes de fuego que a dia de hoy usa contra sus rivales."
    golpes = []


    def __init__(self):

        self.golpes.append(TecnicaP1)

    def mostrar(self):

        print("Nombre: " + self.nombre + "\n"
              "Vida: " + str(self.vida) + "\n"
              "Historia: " + self.descripcion)

    def restvida(self, vidat):

        self.vida = self.vida - vidat

    # def ataque(self, P2, golpe):



    # def esquivar(self):



    def mostrarAtaques(self):

        print(TecnicaP1.golpe1(self),
              TecnicaP1.golpe2(self) ,
              TecnicaP1.golpe3(self))





