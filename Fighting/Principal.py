from Personaje1 import Personaje1
from Personaje2 import Personaje2
from TecnicaP1 import TecnicaP1
from TecnicaP2 import TecnicaP2

def Menu():

      print("------------------------------------------------ \n"
      "Bienvenido a Soul Reaper V escoge tu personaje: \n"
      "------------------------------------------------ \n")

      P1 = Personaje1()

      P2 = Personaje2()

      print("1.")

      P1.mostrar()

      print(" \n"
      "----------------------------------------------------------------------------------------------------------------------------------------------------- \n")

      print("2.")

      P2.mostrar()

      print(" \n"
      "----------------------------------------------------------------------------------------------------------------------------------------------------- \n")

      print("3. Salir")

      opcion = input("\n"
      "----------------------------------------------\n"
      "Pulsa el numero del personaje para escogerlo. \n"
      "----------------------------------------------\n")

      if opcion == "1":

            P1.mostrarAtaques()
            MenuAtaques()

      elif opcion == "2":

            P2.mostrarAtaques()
            MenuAtaques()

      elif opcion == "3":

            exit()

      else:
            print("------------------------------------------------ \n"
            "Por favor escoja una opcion valida: \n"
            "------------------------------------------------")
            Menu()

def MenuAtaques():

      opcion = input("\n"
                     "------------------------------------------------\n"
                     "Pulsa el numero del ataque que quieres realizar. \n"
                     "------------------------------------------------\n")

      if opcion == "1":

            print(TecnicaP1.golpe1())
            MenuAtaques()

      elif opcion == "2":

            print("q paza")
            MenuAtaques()

      elif opcion == "3":

            print("ta luego")
            MenuAtaques()

      else:
            print("------------------------------------------------ \n"
            "Por favor escoja una opcion valida: \n"
            "------------------------------------------------")
            MenuAtaques()


Menu()