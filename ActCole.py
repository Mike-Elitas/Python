bus = 4000
def calcular():
    final = numero*case+bus
    print ("El precio total es: " + str(final))
    print ("El precio por alumno es: " + str(case))
numero = int(input("Introduce el numero de alumnes: "))
if  numero > 100:
    case = 65
    calcular()
elif numero > 49:
    case = 70
    calcular()
elif numero > 29:
    case = 95
    calcular()
elif numero > 0:
    case = 115
    calcular()
else:
    print("El numero es invalido.")
