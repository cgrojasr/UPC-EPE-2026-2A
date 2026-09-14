# Ejercicio 1
# Dados dos números, que determine la suma, resta, multiplicación, división, potencia

import math

def ejercicio1():
    a = 4
    b = 5
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    potencia = a ** b

    print('La suma de los numeros ingresado es: ', suma)
    print('La resta de los numeros ingresado es: ', resta)
    print('La multiplicación de los numeros ingresado es: ', multiplicacion)
    print('La división de los numeros ingresado es: ', division)
    print('La potencia de los numeros ingresado es: ', potencia)

# ejercicio1()

def ejercicio1_1():
    a = int(input('Ingrese el primer numero: '))
    b = int(input('Ingrese el segundo numero: '))
    if b == 0:
        print('No se puede dividir entre cero')
        return
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    potencia = a ** b

    print('La suma de los numeros ingresado es: ', suma)
    print('La resta de los numeros ingresado es: ', resta)
    print('La multiplicación de los numeros ingresado es: ', multiplicacion)
    print('La división de los numeros ingresado es: ', division)
    print('La potencia de los numeros ingresado es: ', potencia)

# ejercicio1_1()

# Fin del ejercicio 1

# Ejercicio 2
# Que determine el Área de un circulo
def ejercicio2():
    radio = 4
    if radio < 0:
        print('El radio no puede ser negativo')
        return
    area = round(math.pi * (radio ** 2), 2)
    print('El área del circulo es: ', area)

# ejercicio2()

def ejercicio2_1():
    radio = float(input('Ingrese el radio del circulo: '))
    if radio < 0:
        print('El radio no puede ser negativo')
        return
    area = round(math.pi * (radio ** 2), 2)
    print('El área del circulo es: ', area)

# ejercicio2_1()

# Fin del ejercicio 2

# Ejercicio 3
# Que solicite la temperatura en grados Celsius y la convierta a grados Fahrenheit.

def ejercicio3():
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    print('La temperatura en grados Fahrenheit es: ', fahrenheit)

# ejercicio3()

def ejercicio3_1():
    celsius = float(input('Ingrese la temperatura en grados Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print('La temperatura en grados Fahrenheit es: ', fahrenheit)

# ejercicio3_1()

# Ejercicio 4
def ejercicio4(): 
    masa1 = 20 
    masa2 = 100 
    distancia = 2 
    if distancia <= 0: 
        print("La distancia no puede menor o igual a cero") 
        return
    if masa1 < 0 or masa2 < 0: 
        print("La masa no puede ser negativa") 
        return
    G = 6.674 * 10 ** -11 
    fuerza_gravitacional = G * masa1 *masa2 /distancia**2 
    print("La fuerza gravitacional es ", fuerza_gravitacional, " Newtons") 

# ejercicio4() 

# Ejercicio 5
def calcular_monedas(cantidad): 
    monedas_5 = cantidad // 5 
    cantidad_resto = cantidad % 5 
    monedas_2 = cantidad_resto // 2 
    monedas_1 = cantidad_resto % 2 
    print ("la cantidad de monedas de 5 es de: ",monedas_5) 
    print ("la cantidad de monedas de 2 es de: ",monedas_2) 
    print ("la cantidad de monedas de 1 es de: ",monedas_1) 

# calcular_monedas(23)
# Ejercicio 6
def ejercicio6(): 
    horassegundos = 151515 
    if horassegundos < 0: 
        print("El tiempo no puede ser negativo") 
        return
    
    horas = horassegundos // 3600 
    resto = horassegundos % 3600 
    minutos = resto // 60 
    segundos = resto % 60 

    print(horassegundos,"son",horas,"Horas", minutos,"Minutos", "y", segundos,"Segundos") 

ejercicio6()