# Ejercicio 3:  buscar un elemento en la matriz.
# Objetivo:

# Solicitar al usuario una matriz de 3 X 3.
# Pedir un número y verificar si se encuentra en la matriz.

matriz = []

for i in range (3):
    fila = []
    for j in range (3):
        valor = int(input(f"Ingrese el valor para la posición [{i}] [{j}]: "))
        fila.append (valor)
    matriz.append (fila)
buscar = int(input("Ingrese el número que va a buscar: "))
enontrado = False

for i in range (len(matriz)):
    for j in range (len(matriz [i])):
        if matriz [i] [j] == buscar:
            print (f"El número {buscar} se encuentra en la posición [{i}] [{j}]")
            enontrado = True
if not enontrado:
    print ("El número no se encuentra en la matriz.")