#Ejercicio 0
# El profesor del curso de Fundamentos de programación a indicado que aquellos alumnos que saquen nota 
# superior a 12 en la PC1 y PC2 automáticamente aprueban el curso, los demás deberán dar Examen Final. 
# Quien de los siguientes alumnos estarán exonerados si a continuación se muestran sus calificaciones?

# Concepto	Juan	Pedro	Luis	Maria	Rosa
# Nota 1	15	10	13	11	18
# Nota 2	13	18	17	12	10

def ejercicio0():
    Nota1_Juan = 15
    Nota1_Pedro = 10
    Nota1_Luis = 13
    Nota1_Maria = 11
    Nota1_Rosa = 18
    Nota2_Juan = 13
    Nota2_Pedro = 18
    Nota2_Luis = 17
    Nota2_Maria = 12
    Nota2_Rosa = 10
    
    
    if Nota1_Juan > 12 and Nota2_Juan > 12:
        print("Juan está exonerado")
    else:
        print("Juan debe dar examen final")

    if Nota1_Pedro > 12 and Nota2_Pedro > 12:
        print("Pedro está exonerado")
    else:
        print("Pedro debe dar examen final")

    if Nota1_Luis > 12 and Nota2_Luis > 12:
        print("Luis está exonerado")
    else:
        print("Luis debe dar examen final")

    if Nota1_Maria > 12 and Nota2_Maria > 12:
        print("Maria está exonerada")
    else:
        print("Maria debe dar examen final")

    if Nota1_Rosa > 12 and Nota2_Rosa > 12:
        print("Rosa está exonerada")
    else:
        print("Rosa debe dar examen final")

# ejercicio0()

# Ejercicio 1
# Desarrollar un programa que reciba como parámetro 2 números e imprima el mensaje respectivo:
# Si  numero 1 es mayor que numero 2 imprimir “A es mayor a B”
# Si  numero 1 es menor que numero 2 imprimir “A es menor a B”
# Si  numero 1 es igual a 2 imprimir “A es igual a B”

def ejercicio1(num1, num2):
    print("El valor de A es: ", num1, " y el valor de B es: ", num2)
    # SWITCH
    print("---------------Usando SWITCH---------------")
    if num1 > num2:
        print("A es mayor a B")
    elif num1 < num2:
        print("A es menor a B")
    else:
        print("A es igual a B")
    # IF
    print("---------------Usando IF---------------")
    if num1 > num2:
        print("A es mayor a B")
    if num1 < num2:
        print("A es menor a B")
    if num1 == num2:
        print("A es igual a B")

# ejercicio1(5, 10)
# ejercicio1(10, 5)
# ejercicio1(20, 20)

# Ejercicio 2
# Que reciba un numero y muestre un mensaje indicando si es par o no.
def ejercicio2(num):
    if num % 2 == 0:
        print("El número ", num, " es par")
    else:
        print("El número ", num, " es impar")

ejercicio2(5)
ejercicio2(10)

# Ejercicio 5-1
# El presidente de un club de fútbol requiere calcular el sueldo de sus jugadores si se tiene 
# como dato la edad y nacionalidad del jugador.
# Además, se sabe que el sueldo se calcula de la siguiente manera:
# Sueldo fijo: 2500 soles
# Si es extranjero recibe un bono de 500 soles
# Si la edad está entre 15 y 20 el sueldo se incrementa en 1400 soles
# Si la edad está entre 21 y 25 el sueldo se incrementa en 1500 soles
# Si la edad está entre 26 y 30 el sueldo se incrementa en 1200 soles
# En otros casos el sueldo se incrementará en 800 soles
# Se pide elaborar un programa en Python que permita determinar el sueldo de un jugador si se 
# tienen como datos su edad y nacionalidad (E: Extranjero; N: Nacional).

def ejercicio5_1(edad, nacionalidad):
    # Sueldo base
    sueldo = 2500

    # Validando nacionalidad
    nacionalidad = nacionalidad.upper()
    if nacionalidad != "E" and nacionalidad != "N":
        print("Nacionalidad inválida")
        return
    if nacionalidad == "E":
        sueldo += 500

    # Validando edad
    if 15 <= edad and edad <= 20:
        sueldo += 1400
    elif 21 <= edad and edad <= 25:
        sueldo += 1500
    elif 26 <= edad and edad <= 30:
        sueldo += 1200
    else:
        sueldo += 800

    print("El sueldo del jugador es: ", sueldo)

# ejercicio5_1(18, "E")
# ejercicio5_1(22, "N")

# Ejercicio 5-2
# Una tienda de venta de productos agrícolas al por mayor le ha solicitado que elabore un 
# programa que permita generar la boleta de venta de los clientes que en ella compran.
# Cuando el cliente realiza la compra se le solicita el tipo de producto y la cantidad de sacos 
# que comprará.
# Los productos que vende dicha tienda son:
# Tipo	Producto	Precio x saco
# P	Papa	20.5
# C	Cebolla	19.4
# L	Limón	32.3
# A	Ají	16.5
# M	Maíz	19.8

# Se le solicita que elabore un programa en Ruby que reciba como datos el tipo de producto y 
# la cantidad de sacos que el cliente comprará y nos determine e imprima el monto que deberá 
# pagar este.
# Debe validar los datos de entrada para una correcta ejecución de su programa.
