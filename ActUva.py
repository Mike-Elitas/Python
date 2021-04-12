precio = 100
def tipo():
    print ("1.Tamaño 1")
    print ("1.Tamaño 2")
    tipo1 = int(input("Selecciona el tipo: "))
    if tipo1 == 1:
        precioFinal = precio+tam1
        print (precioFinal)
    elif tipo1 == 2:
        precioFinal = precio+tam2
        print (precioFinal)
    else:
        print ("No has elegido ningun tipo valido")
print ("1. Tipo A")
print ("2. Tipo B")
tipo2 = int(input("Selecciona el tipo: "))
if tipo2 == 1:
    tam1 = 20
    tam2 = 30
    tipo()
elif tipo2 == 2:
    tam1 = -30
    tam2 = -50
    tipo()
else:
    print ("No has elegido ningun tipo valido")
