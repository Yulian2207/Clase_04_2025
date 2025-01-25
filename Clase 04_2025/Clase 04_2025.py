# Matrices:
# Es una estructura bidimensional que organiza elementos en filas y columnas, esto crea una base de datos.
# Cada posisción dentro de la matriz esta indicada por dos indices ele indice de la fila y el indice de la columna
# esto permite acceder a los datos de una manera rapidoa y eficiente simplificando
# una matriz es una coleccion de arreglo unidimensionales dispuestos en varias fila.

# ¿Como se ve una matriz de 3 X 3?
# [1] [2] [3]
# [4] [5] [6]
# [7] [8] [9]
# Características:
# Tienen dos o mas dimensiones con un número definido de filas y columnas, se puede extender a más dimensiones.

# Indexación:
# Cada elemento tiene una ubicación unica representada por dos indices [filas] [columnas].

# Homogeneas:
# Suelen tener elementos del mismo tipo de datos ya sean enteros, flotantes, catacteres, booleanos etc.

# Estrictura contigua:
# Se almacenan en bloques contiguos de memoria, lo que permite el acceso eficiente de los datos.

# Usos maás frecuentes:
# Usadas en ciencia de datos, grafícos de computadora; bases de datos y otras opciones.

# Ejemplos prectícos de usos en matrices en la vida real...
# Las matrices se suelen usar en una variedad de casos como.
# Tablas de datos:
# Almacenar las notas de estudiantes de diferentes materias.

# Imagenes digítales:
# Las imagenes son matrices formadas de pixeles, estos pixeles pueden representarse como arreglos de valores de color.

# Juegos de video:
# Un ajedrez es una matriz de 8 X 8.

# Algoritmos matemáticos:
# Se usan en algebra líneal, simulaciones y calculos estadicos.

# Representaciones de matrices en progrmación:
# En algunos lenguajes como los compilados, no interpretados, de tipado fuerte como Java o C las matrices tienen
# una estructura rigida, donde al principio se debe aclarar el tema en filas y columnas.
# Esto es de anera fija. En Python, las matrices son más flexibles y se implementan con listas anidadas.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print (matriz)
print (matriz [0])
print (matriz [1] [2])

# ¿Como acceder a unos elementos de una matriz?:
# Para acceder a ellos o un elemento especifíco usamos sus indíce, el primero SIEMPRE va a ser el de la fila
# (Los arreglos interiores). Y el segundo SIEMPRE va a ser el de la columna (los elementos de los arreglos interiores)

elemento = matriz [2] [1]
print (f"Elemento {elemento}")

# ¿Como se recorren la matrices?
# Se recorren con un for dentro de un for.

for i in range (len(matriz)): #Recorrer filas
    for j in range (len(matriz[i])):
        print (f"Elemnto en la fila {i} en la columna {j} es: {matriz [i] [j]}")

# Puedo modificar valores en la matriz.
# Podemos cambiar un valor accediendo directamente por la posicición.

matriz [1] [1] = 99
print (f"La matriz ha quedado asi: {matriz}") 

# Operaciones más comunes con matrices.
# Algunas operaciones importantes que se pueden realizar 