# El supermercado UNO está premiando a sus clientes que compran por un monto mayor a 800 soles, el premio consiste en un juego, donde el cliente, extrae de una 
# urna un papel que tiene un numero de varias cifras (el número de cifras es variado), como máximo tiene 9 dígitos. 
#  
# El cliente va a recibir un premio de acuerdo a la cantidad de unos que aparece en el papel.
#  
# Si no hay ningún digito uno, no recibe ningún premio. 
# Si hay un digito uno va a recibir el 1% de descuento de la compra realizada.
# Si hay dos dígitos uno va a recibir el 2% de descuento de la compra realizada.
# Si hay tres dígitos uno va a recibir el 3% de descuento de la compra realizada.
# Si hay cuatro dígitos uno va a recibir el 4% de descuento de la compra realizada.
# Y así sucesivamente hasta llegar a los 9 dígitos uno.
# Si la cantidad de  dígitos uno es 2 o múltiplo de 2 recibe un descuento adicional de 50 soles.
#  
# Calcular el descuento total que recibe un cliente
# Calcular el importe a pagar.

# Numero que se le dara al cliente es aleatorio y se genera con la función numero_papelito_aleatorio().
def numero_papelito_aleatorio():
    import random
    numero = random.randint(0, 999999999)
    return numero

def calcular_descuento(cantidad_unos):
    descuento = cantidad_unos * 0.01  # 1% por cada dígito uno
    return descuento

def calcular_descuento_adicional(cantidad_unos):
    if cantidad_unos >= 2 and cantidad_unos % 2 == 0:
        return 50  # Descuento adicional de 50 soles
    return 0

def calcular_importe_a_pagar(monto_compra, descuento, descuento_adicional):
    descuento_total = monto_compra * descuento + descuento_adicional
    importe_a_pagar = monto_compra - descuento_total
    return importe_a_pagar, descuento_total

def imprimir_resultados():
    monto_compra = float(input("Ingrese el monto de compra: "))
    
    if monto_compra < 800:
        print("El monto de compra debe ser mayor a 800 soles para recibir un premio.")
        return

    numero = numero_papelito_aleatorio()
    print("Número del papelito:", numero)
    cantidad_unos = 0
    # Contar la cantidad de dígitos uno en el número generado
    # cantidad_unos = numero.count('1') 
    # Estructura repetitiva para contar la cantidad de dígitos uno en el número generado
    for digito in str(numero):
        if digito == '1':
            cantidad_unos += 1
    descuento = calcular_descuento(cantidad_unos)
    descuento_adicional = calcular_descuento_adicional(cantidad_unos)
    importe_a_pagar, descuento_total = calcular_importe_a_pagar(monto_compra, descuento, descuento_adicional)
    print("Cantidad de dígitos uno:", cantidad_unos)
    print("Descuento total:", descuento_total)
    print("Importe a pagar:", importe_a_pagar)

# imprimir_resultados()  # Ejemplo de monto de compra

# Una empresa tiene como reglamento dar aumento de sueldo a sus trabajadores todos los años, 
# el porcentaje de aumento está dado de acuerdo al tipo de trabajador: Gerente (g) o empleado (e). 
# Los gerentes reciben un aumento del 14% anual y los empleados reciben el 8% anual. Cada 4 años en vez de 14% 
# reciben 18% y en vez de 8% reciben 12% (dependiendo del tipo de trabajador). Desarrollar los módulos que determinen 
# el sueldo que tendrá un trabajador después de N años y el porcentaje de aumento de sueldo que ha obtenido comparando 
# su sueldo original y su sueldo después de N años. Tenga en cuenta que los aumentos obtenidos van a su sueldo. 
#  
# Se le solicita lo siguiente:
# Calculo del sueldo después de N años					
# Calcular el porcentaje de aumento después de N años.				
# Calcular la suma del sueldo de un gerente y de un empleado después de N años. 

def calcular_sueldo_despues_de_n_anios(sueldo_trabajador, sueldo_gerente, n_anios):
    for anio in range(1, n_anios + 1):
        if anio % 4 == 0:
            sueldo_trabajador += sueldo_trabajador * 0.12  # Aumento del 12% para empleados cada 4 años
            sueldo_gerente += sueldo_gerente * 0.18  # Aumento del 18% para gerentes cada 4 años
        else:
            sueldo_trabajador += sueldo_trabajador * 0.08  # Aumento del 8% para empleados
            sueldo_gerente += sueldo_gerente * 0.14  # Aumento del 14% para gerentes
    return sueldo_trabajador, sueldo_gerente

def calcular_porcentaje_aumento(sueldo_original, sueldo_final):
    aumento = sueldo_final - sueldo_original
    porcentaje_aumento = (aumento / sueldo_original) * 100
    return porcentaje_aumento

def calcular_suma_sueldos(sueldo_gerente, sueldo_empleado):
    return sueldo_gerente + sueldo_empleado

def imprimir_resultados_sueldos():
    sueldo_gerente = float(input("Ingrese el sueldo del gerente: "))
    sueldo_empleado = float(input("Ingrese el sueldo del empleado: "))
    n_anios = int(input("Ingrese la cantidad de años proyectados: "))

    sueldo_empleado_final, sueldo_gerente_final = calcular_sueldo_despues_de_n_anios(sueldo_empleado, sueldo_gerente, n_anios)
    porcentaje_aumento_gerente = calcular_porcentaje_aumento(sueldo_gerente, sueldo_gerente_final)
    porcentaje_aumento_empleado = calcular_porcentaje_aumento(sueldo_empleado, sueldo_empleado_final)
    suma_sueldos = calcular_suma_sueldos(sueldo_gerente_final, sueldo_empleado_final)
    
    print("\nResultados después de", n_anios, "años:")
    print(f"Sueldo del gerente después de {n_anios} años: {round(sueldo_gerente_final, 2)}")
    print(f"Porcentaje de aumento del gerente: {round(porcentaje_aumento_gerente, 2)}%")
    print(f"Sueldo del empleado después de {n_anios} años: {round(sueldo_empleado_final, 2)}")
    print(f"Porcentaje de aumento del empleado: {round(porcentaje_aumento_empleado, 2)}%")
    print(f"Suma de sueldos después de {n_anios} años: {round(suma_sueldos, 2)}")

imprimir_resultados_sueldos()