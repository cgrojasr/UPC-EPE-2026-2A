#Ejercicio 1: Etiquetado de productos
# Una reconocida empresa que se dedica al rubro logístico de almacén acaba de 
# implementar un proceso automático de etiquetado de todos los productos que 
# almacenará. Las etiquetas poseen el siguiente formato:

# Posición	        Significado     
# Posición 1 a la 2	País de procedencia del producto
#                     PE: Perú
#                     AR: Argentina
#                     CH: Chile
#                     BR: Brasil
# Posición 3 a la 6	Correlativo de productos ingresado
# Posición 7 a la 8	Costo de almacenamiento diario del producto

# Ejemplo:
# PE219002 
# • PE = País de procedencia Perú
# • 2190 = existen 2190 productos similares en el almacén
# • 02 = 2 soles cuestan almacenar el producto en el almacén

# Se solicita lo siguiente:

# 1. Subprograma que obtenga la cantidad de productos de una determinada nacionalidad.
# 2. Subprograma que obtenga el último correlativo generado para un producto de una 
# determinada nacionalidad.
# 3. Subprograma que obtenga el monto de almacenar la totalidad de productos de una 
# determinada nacionalidad en el almacén.

def main():
    # Arreglo con 50 códigos de productos
    # codigos = ["PE101010","PE633296","PE523412","PE395656","PE764248",
    #            "AR202020","AR202120","AR202220","AR202320","AR202520",
    #            "CH304030","CH303930","CH303830","CH303730","CH303630",
    #            "BR404041","BR404044","BR404048","BR404042","BR404045"]

    codigos = [""]*50
    indice = 0
    while True:
        print('1. Ingresar código de producto')
        print('2. Obtener cantidad de productos por nacionalidad')
        print('3. Obtener último correlativo por nacionalidad')
        print('4. Obtener monto de almacenamiento por nacionalidad')
        print('5. Salir')
        opcion = input('Ingrese una opción: ')
        if opcion == '1':
            if indice >= 50:
                print('No se pueden ingresar más códigos de productos')
                break
            ingresar_codigo(codigos, indice)
        elif opcion == '2':
            obtener_cantidad(codigos)
        elif opcion == '3':
            obtener_correlativo(codigos)
        elif opcion == '4':
            obtener_monto(codigos)
        elif opcion == '5':
            break
        else:
            print('Opción inválida')

def ingresar_codigo(codigos, indice):
    salir = False
    while not salir:
        codigo = input('Ingrese el código del producto: ')
        if len(codigo) != 8:
            print('El código debe tener 8 caracteres')
            continue    
        # indice = len(codigos)
        codigos[indice] = codigo
        indice += 1
        salir_respuesta = input('Desea ingresar otro código? (s/n): ')
        if salir_respuesta.lower() != 's':
            salir = True
        else:
            salir = False

def obtener_cantidad(codigos):
    nacionalidad = input('Ingrese la nacionalidad (PE, AR, CH, BR): ')
    cantidad = 0
    for codigo in codigos:
        if codigo[0:2] == nacionalidad:
            cantidad += 1
    print('La cantidad de productos de la nacionalidad', nacionalidad, 'es:', cantidad)

def obtener_correlativo(codigos):
    nacionalidad = input('Ingrese la nacionalidad (PE, AR, CH, BR): ')
    correlativos = {}
    for codigo in codigos:
        if codigo[0:2] == nacionalidad:
            correlativos[codigo] = int(codigo[2:6])
    if len(correlativos) == 0:
        print('No hay productos de la nacionalidad', nacionalidad)
    else:
        print('El último correlativo de la nacionalidad', nacionalidad, 'es:', max(correlativos))

def obtener_monto(codigos):
    nacionalidad = input('Ingrese la nacionalidad (PE, AR, CH, BR): ')
    monto = 0
    for codigo in codigos:
        if codigo[0:2] == nacionalidad:
            monto += int(codigo[6:8])
    print('El monto de almacenamiento de la nacionalidad', nacionalidad, 'es:', monto)

# main()


# Ejercicio 2: Validación de códigos de producto
# Una empresa utiliza códigos de producto con el siguiente formato:
# LLNNNLLL
# Donde:
# •	LL = dos letras que indican la categoría
# •	NNN = tres dígitos que indican el lote
# •	LLL = tres letras que indican el almacén de destino
# Ejemplos válidos:
# •	EL120SUR
# •	AL450NTE
# •	RO999CTR
# El programa debe:
# 1.	Validar que el código tenga exactamente 8 caracteres.
# 2.	Validar que los primeros 2 sean letras y los siguientes 3 sean números.
# 3.	Extraer: 
# o	Categoría → código[0:2]
# o	Lote → código[2:5]
# o	Almacén → código[5:8]
# 4.	Clasificar la categoría según estas reglas: 
# o	EL → Electrónica
# o	AL → Alimentos
# o	RO → Ropa
# o	OT → Categoría desconocida
# 5.	Mostrar un mensaje final con toda la información extraída.

def validar_codigo(codigo):
    if len(codigo) != 8:
        print('El código debe tener 8 caracteres')
        return False
    if not codigo[0:2].isalpha():
        print('Los primeros 2 caracteres deben ser letras')
        return False
    if not codigo[2:5].isdigit():
        print('Los siguientes 3 caracteres deben ser números')
        return False
    if not codigo[5:8].isalpha():
        print('Los últimos 3 caracteres deben ser letras')
        return False
    return True

def extraer_informacion(codigo):
    categoria = codigo[0:2]
    lote = codigo[2:5]
    almacen = codigo[5:8]
    return categoria, lote, almacen

def clasificar_categoria(categoria):
    if categoria == 'EL':
        return 'Electrónica'
    elif categoria == 'AL':
        return 'Alimentos'
    elif categoria == 'RO':
        return 'Ropa'
    else:
        return 'Categoría desconocida'

def main_validar_codigo():
    codigo = input('Ingrese el código del producto: ')
    if validar_codigo(codigo):
        categoria, lote, almacen = extraer_informacion(codigo)
        categoria_clasificada = clasificar_categoria(categoria)
        print('Categoría:', categoria_clasificada)
        print('Lote:', lote)
        print('Almacén:', almacen)

main_validar_codigo()




