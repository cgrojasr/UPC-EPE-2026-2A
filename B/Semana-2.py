# Que calcule y muestre la fuerza de atracción gravitacional entre dos masas, M1 y M2 situadas a una distancia R. 
# Donde las masas se expresan en kilogramos y la distancia en metros y la constante de gravitación universal tiene el valor de: 
# G=6.67*10^-11 Nw*m2/Kg2

def ejercicio4():
    # Masa de la Tierra en kilogramos
    masa1 = 5.9722 * 10**24 
    masa2 = 70 
    distancia = 2 
    if distancia <= 0: 
        print("La distancia no puede menor o igual a cero") 
        return
    if masa1 < 0 or masa2 < 0: 
        print("La masa no puede ser negativa") 
        return
    G = 6.674 * 10 ** -11 
    fuerza_gravitacional = round(G * masa1 *masa2 /distancia**2, 2)
    print("La fuerza gravitacional es ", fuerza_gravitacional, " Newtons")

# ejercicio4()


# Una empresa pequeña genera recibos de pago manualmente.
#  Se desea automatizar el proceso mediante un programa que:

# Reciba como entrada: nombre del trabajador, horas trabajadas y tarifa por hora.
# Calcule el sueldo bruto.
# Aplique un descuento del 8% a todos los trabajadores
# Genere como salida un recibo con:
# Nombre
# Horas trabajadas
# Sueldo bruto
# Descuento
# Sueldo neto

def ejercicio5():
    nombre = input("Ingrese el nombre del trabajador: ")
    horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
    tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))

    if horas_trabajadas < 0 or tarifa_por_hora < 0:
        print("Las horas trabajadas y la tarifa por hora no pueden ser negativas.")
        return

    sueldo_bruto = horas_trabajadas * tarifa_por_hora
    descuento = sueldo_bruto * 0.08
    sueldo_neto = sueldo_bruto - descuento

    print("\nRecibo de Pago")
    print("Nombre del trabajador:", nombre)
    print("Horas trabajadas:", horas_trabajadas)
    print("Sueldo bruto: $", round(sueldo_bruto, 2))
    print("Descuento (8%): $", round(descuento, 2))
    print("Sueldo neto: $", round(sueldo_neto, 2))

ejercicio5()