# Ejercicio de recorrido de un arreglo
arr = [1, 2, 3, 4, 5]
for i in range(1, len(arr), 1):
    print(arr[i])

# Pregunta 2
variable = "5"
convertir_entero = int(variable)

# Pregunta 3
# for = "perro"
# print(for)  # Esto imprimirá "perro" porque la variable 'int' ha sido sobrescrita

# Pregunta 4
# while es condicional
opcion = 1
while opcion == 5:
    print("Opción válida")

# Pregunta 5
# if sirve para agregar condicion en el codigo
if opcion == 1:
    print("Opción 1 seleccionada")
else:
    print("Opción no válida")

# Pregunta 6
6**2 
# potencia y el resultado es 36
6//2
# división entera y el resultado es 3
6%2
# módulo y el resultado es 0 (residuo de la división)

# Pregunta 7
# No se puede convertir un string a int si el string no representa un número válido. Por ejemplo, intentar convertir "abc" a int generará un error.

# Pregunta 8
# Repasar bien el uso de arreglos en un iteracion
def suma(a, b):
    return a + b

# Pregunta 9
# print(variable[6:9])
#           123456789012 
variable = "La U es la U"

# Pregunta 10
for i in range(100, 20, -40):  
    print(i)
# 100, 60, 20

# Pregunta 11
# FOR cuando sabes cuantas veces tienes que repetir el ciclo
# WHILE cuando no sabes cuantas veces tienes que repetir el ciclo

# Pregunta 12
# como se denomina al valor de n en un funcion
def factorial(n):
    a = 0
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


