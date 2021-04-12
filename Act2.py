a = int(input("Introduce un numero entre 0 y 100 "))
b = int(input("Introduce otro numero entre 0 y 100 "))
suma = a + b
resta = a - b
multiplica = a * b
divide = a / b
print ("1. Sumar")
print ("2. Restar")
print ("3. Multiplicar")
print ("4. Dividir")
option = int(input("Selecciona una de las opciones anteriores: "))
if option == 1:
    print(suma)
elif option == 2:
    print(resta)
elif option == 3:
    print (multiplica)
elif option == 4:
    print (divide)
else:
    print ("Escoge una opción válida")
