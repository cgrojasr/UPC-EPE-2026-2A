# Ejercicio: Ventas mensuales
# Una empresa vendedora de fotocopiadoras necesita calcular cual ha sido el volumen de ventas de cada 
# uno de sus agentes comerciales durante el presente mes y en base a eso determinar distintos indicadores, 
# así como montos a pagar en comisión de ventas.
	
# Se le solicita:
# Obtener el total de unidades vendidas durante el presente mes. Para eso se tiene como dato de entrada un 
# arreglo con la cantidad de unidades vendidas por cada agente comercial.
# Si se sabe que la cuota de venta de cada vendedor es 5 unidades, determinar cuál es el porcentaje de 
# vendedores que superaron la cuota de venta. Para eso se tiene como dato de entrada un arreglo con la 
# cantidad de unidades vendidas por cada agente comercial.
# Se desea saber quién(es) fueron los agentes de ventas que superaron la cuota de venta.
# Si se sabe que por cada unidad vendida se tiene que pagar una comisión de ventas de 300 soles, determinar 
# cuánto es lo que se tiene que pagar como comisión este mes.

def main():
    # Datos de entrada: arreglo con la cantidad de unidades vendidas por cada agente comercial
    ventas_agentes = registro_ventas()  # Llamada a la función para registrar las ventas de los agentes
    # ventas_agentes = [3, 7, 5, 10, 2, 6, 8]  # Ejemplo de ventas por agente

    # Calcular el total de unidades vendidas durante el presente mes
    total_unidades_vendidas = sum(ventas_agentes)
    print("Total de unidades vendidas:", total_unidades_vendidas)

    # Identificar quiénes fueron los agentes de ventas que superaron la cuota de venta
    imprimir_agentes_superaron_cuota(ventas_agentes)

    # Determinar el porcentaje de vendedores que superaron la cuota de venta (5 unidades)
    calcular_porcentaje_superaron_cuota(ventas_agentes)

    # Calcular el monto a pagar en comisión de ventas (300 soles por unidad vendida)
    calcular_monto_comision(total_unidades_vendidas)

def registro_ventas():
    # Función para registrar las ventas de los agentes comerciales
    # Aquí se puede implementar la lógica para ingresar las ventas de cada agente
    cantidad_agentes = int(input("Ingrese la cantidad de agentes comerciales: "))
    ventas_agentes = [0] * cantidad_agentes
    for i in range(cantidad_agentes):
        ventas_agentes[i] = int(input(f"Ingrese la cantidad de unidades vendidas por el agente {i + 1}: "))
    return ventas_agentes

def calcular_monto_comision(total_unidades_vendidas):
    comision_por_unidad = 300
    monto_comision_total = total_unidades_vendidas * comision_por_unidad
    print("Monto total a pagar en comisión este mes:", monto_comision_total, "soles")

def calcular_porcentaje_superaron_cuota(ventas_agentes):
    cuota_venta = 5
    vendedores_superaron_cuota = 0
    for ventas in ventas_agentes:
        if ventas > cuota_venta:
            vendedores_superaron_cuota += 1
    porcentaje_superaron_cuota = round((vendedores_superaron_cuota / len(ventas_agentes)) * 100, 2)
    print("Porcentaje de vendedores que superaron la cuota de venta:", porcentaje_superaron_cuota, "%")

def imprimir_agentes_superaron_cuota(ventas_agentes):
    cuota_venta = 5
    for i in range(len(ventas_agentes)):
        ventas = ventas_agentes[i]
        if ventas > cuota_venta:
            print(f"El agente {i + 1} superó la cuota de venta con {ventas} unidades vendidas.")

# main()


# Enunciado
# Una universidad desea analizar el rendimiento de un grupo de estudiantes. El programa debe:
# Solicitar al usuario cuántos estudiantes tiene el curso.
# Crear un arreglo con las notas de cada estudiante (entre 0 y 20).
# Calcular:
    # La nota promedio del curso.
    # La nota máxima y el índice del estudiante que la obtuvo.
    # La nota mínima y el índice del estudiante que la obtuvo.
# Crear un segundo arreglo con las notas aprobadas (≥ 11).
    # Determinar:
        # El porcentaje de aprobados.
        # El porcentaje de desaprobados.
# Mostrar:
    # Lista completa de notas
    # Lista de aprobados

def ejercicio_2():
    notas_estudiantes = registrar_notas()  # Llamada a la función para registrar las notas de los estudiantes
    print("----------------------------------------------------")
    nota_promedio = round(sum(notas_estudiantes) / len(notas_estudiantes), 2)
    print("Nota promedio del curso:", nota_promedio)
    imprimir_notas_maximas(notas_estudiantes)
    imprimir_notas_minimas(notas_estudiantes)
    cantidad_aprobados = obtener_cantidad_aprobados(notas_estudiantes)
    notas_aprobadas = filtrar_notas_aprobadas(notas_estudiantes, cantidad_aprobados)
    porcentaje_aprobados = round((cantidad_aprobados / len(notas_estudiantes)) * 100, 2)
    porcentaje_desaprobados = round(100 - porcentaje_aprobados, 2)
    print("----------------------------------------------------")
    print("Cantidad de estudiantes aprobados:", cantidad_aprobados)
    print("Porcentaje de aprobados:", porcentaje_aprobados, "%")
    print("Porcentaje de desaprobados:", porcentaje_desaprobados, "%")
    print("----------------------------------------------------")
    for i in range(len(notas_estudiantes)):
        print(f"Estudiante {i + 1}: Nota = {notas_estudiantes[i]}")
    print("----------------------------------------------------")
    for i in range(len(notas_aprobadas)):
        print(f"Estudiante aprobado {i + 1}: Nota = {notas_aprobadas[i]}")



def registrar_notas():
    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
    notas_estudiantes = [0] * cantidad_estudiantes
    for i in range(cantidad_estudiantes):
        nota_estudiante = -1  # Inicializar con un valor fuera del rango válido
        while nota_estudiante < 0 or nota_estudiante > 20:
            nota_estudiante = float(input(f"Ingrese la nota del estudiante {i + 1} (entre 0 y 20): "))
            if nota_estudiante < 0 or nota_estudiante > 20:
                print("La nota debe estar entre 0 y 20. Intente nuevamente.")
        notas_estudiantes[i] = nota_estudiante

    return notas_estudiantes

def imprimir_notas_maximas(notas_estudiantes):
    nota_maxima = max(notas_estudiantes)
    print("----------------------------------------------------")
    print("La nota máxima es:", nota_maxima)
    for i in range(len(notas_estudiantes)):
        if notas_estudiantes[i] == nota_maxima:
            print(f"La nota máxima la obtuvo el estudiante {i + 1}.")

def imprimir_notas_minimas(notas_estudiantes):
    nota_minima = min(notas_estudiantes)
    print("----------------------------------------------------")
    print("La nota mínima es:", nota_minima)
    for i in range(len(notas_estudiantes)):
        if notas_estudiantes[i] == nota_minima:
            print(f"La nota mínima la obtuvo el estudiante {i + 1}.")

def filtrar_notas_aprobadas(notas_estudiantes, cantidad_aprobados):
    notas_aprobadas = [0] * cantidad_aprobados
    i = 0
    for nota in notas_estudiantes:
        if nota >= 11:
            notas_aprobadas[i] = nota
            i += 1 
    return notas_aprobadas

def obtener_cantidad_aprobados(notas_estudiantes):
    cantidad_aprobados = 0
    for nota in notas_estudiantes:
        if nota >= 11:
            cantidad_aprobados += 1
    return cantidad_aprobados

ejercicio_2()