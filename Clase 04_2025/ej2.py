# Ejercicio 2: Suma los elementos de un amatriz.
# Crera una matriz de 3 X 3
# 

matriz = [
    [2, 3, 1],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0
for i in range (3):
    for j in range (3):
        suma += matriz  [i] [j]
print ("La suma de los elementos es: ", suma)

