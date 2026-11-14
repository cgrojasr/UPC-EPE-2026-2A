# Una tienda de venta de productos agrícolas al por mayor le ha solicitado que elabore un programa que permita generar la boleta de venta de los clientes que en ella compran.
# Cuando el cliente realiza la compra se le solicita el tipo de producto y la cantidad de sacos que comprará.
# Los productos que vende dicha tienda son:

# Tipo	Producto	Precio x saco
# P	    Papa	    20.5
# C	    Cebolla	    19.4
# L	    Limón	    32.3
# A	    Ají	        16.5
# M	    Maíz	    19.8

# Se le solicita que elabore un programa en Ruby que reciba como datos el tipo de producto y la cantidad de sacos que el cliente comprará y nos determine e imprima el monto que deberá pagar este.
# Debe validar los datos de entrada para una correcta ejecución de su programa.


def menu_productos():
    print("Bienvenido a la tienda de productos agrícolas")
    print("Seleccione el tipo de producto que desea comprar:")
    print("P - Papa")
    print("C - Cebolla")
    print("L - Limón")
    print("A - Ají")
    print("M - Maíz")

    cod_producto = input("Ingrese el código del producto (P, C, L, A, M): ").upper()

    # validar la opción ingresada por el usuario
    if cod_producto not in ['P', 'C', 'L', 'A', 'M']:
        print("Opción inválida. Por favor, seleccione un producto válido.")
        return None

    return cod_producto

def obtener_precio(cod_producto):
    precios = {
        'P': 20.5,
        'C': 19.4,
        'L': 32.3,
        'A': 16.5,
        'M': 19.8
    }
    return precios.get(cod_producto.upper(), 0)

def calcular_monto(cod_producto, cantidad):
    precio_unitario = obtener_precio(cod_producto)
    monto_total = precio_unitario * cantidad
    return monto_total

def main():
    cod_producto = menu_productos()
    if cod_producto is None:
        return

    try:
        cantidad = int(input("Ingrese la cantidad de sacos que desea comprar: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
    except Exception as e:
        print(f"Entrada inválida. Por favor, ingrese un número entero. Error: {e}")
        return

    monto_total = calcular_monto(cod_producto, cantidad)
    print(f"El monto total a pagar por {cantidad} sacos de producto {cod_producto} es: S/. {monto_total:.2f}")

# main()  

# Enunciado III

# Una empresa de software vende aplicaciones para celulares (iPhone y Android) y requiere un programa que 
# genere el resumen por cada venta realizada.
# Los productos que vende dicha empresa son:

# Tipo	Producto	Tipo de Celular	Precio x unidad
# OI    Oficina	    iPhone	        50.60
# OA    Oficina	    Android	        20.30
# JI    Juegos	    iPhone	        90.80
# JA    Juegos	    Android	        40.50
# UI    Utilitarios	iPhone	        60.50
# UA    Utilitarios	Android	        30.60

# Asimismo, el programa solicita la cantidad de aplicaciones que el cliente va a comprar.
# Se le solicita que elabore un programa en Python que reciba como datos el tipo de producto, 
# el tipo de celular (i: iPhone; A: Android) y la cantidad de unidades que el cliente comprará y 
# nos determine e imprima el monto que deberá pagar este.
# Debe validar los datos de entrada para una correcta ejecución de su programa.

def menu_aplicaciones():
    print("Bienvenido a la tienda de aplicaciones para celulares")
    print("Seleccione el tipo de producto que desea comprar:")
    print("OI - Oficina (iPhone)")
    print("OA - Oficina (Android)")
    print("JI - Juegos (iPhone)")
    print("JA - Juegos (Android)")
    print("UI - Utilitarios (iPhone)")
    print("UA - Utilitarios (Android)")

    cod_producto = input("Ingrese el código del producto (OI, OA, JI, JA, UI, UA): ").upper()

    # validar la opción ingresada por el usuario
    if cod_producto not in ['OI', 'OA', 'JI', 'JA', 'UI', 'UA']:
        print("Opción inválida. Por favor, seleccione un producto válido.")
        return None

    return cod_producto

def obtener_precio_aplicacion(cod_producto):
    precios = {
        'OI': 50.60,
        'OA': 20.30,
        'JI': 90.80,
        'JA': 40.50,
        'UI': 60.50,
        'UA': 30.60
    }
    return precios.get(cod_producto.upper(), 0)

def calcular_monto_aplicacion(cod_producto, cantidad):
    precio_unitario = obtener_precio_aplicacion(cod_producto)
    monto_total = precio_unitario * cantidad
    return monto_total

def main_aplicaciones():
    cod_producto = menu_aplicaciones()
    if cod_producto is None:
        return

    try:
        cantidad = int(input("Ingrese la cantidad de unidades que desea comprar: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
    except Exception as e:
        print(f"Entrada inválida. Por favor, ingrese un número entero. Error: {e}")
        return

    monto_total = calcular_monto_aplicacion(cod_producto, cantidad)
    print(f"El monto total a pagar por {cantidad} unidades del producto {cod_producto} es: S/. {monto_total:.2f}")