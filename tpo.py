import random
"""Una empresa que se dedica al alquiler de autos en una ciudad turística, tiene diferentes
costos según el tipo de auto y la cantidad de KM realizados por los clientes. Todos los
meses, tienen que generar la facturación de los clientes del mes, el cual se calcula según
la cantidad de KM que realizó y el tipo de auto que alquiló y para ello cuentan con la
siguiente información:
Además, se sabe que, por la cantidad de vehículos disponibles, la cantidad de clientes
máximos por mes es de 450, pero el mínimo es siempre 200. También, la cantidad de
Km mínimos que realiza cada cliente es de 100 Km, siendo un máximo de 5000 Km.
La empresa cuenta con el detalle de todos los clientes del mes, el tipo de vehículo y la
cantidad de KM que realizaron. Necesita que se calcule la facturación de cada uno y
poder, de esta forma responder las siguientes necesidades:
● Total de la facturación del mes, cuántos vehículos fueron y el costo asociado.
● Total de facturación por tipo de vehículo, la cantidad de KM, el costo asociado
ordenado por facturación.
● Listado completo detallado del total facturado de cada cliente con su tipo de
vehículo, ordenado facturación.
● Poder seleccionar un tipo de vehículo y que se detallen la facturación, la
cantidad de clientes y el costo del tipo de vehículo seleccionado.
"""
# Constantes
VEHICULOS = ["Chico", "Mediano", "Grande", "Camioneta 4x4", "Van"]
MIN_CLIENTES = 200
MAX_CLIENTES = 450
MIN_KM = 100
MAX_KM = 5000
PRECIO_FIJO_HASTA_1000KM = [7500, 8500,9500,10000,12000]
PRECIO_ADICIONAL_HASTA_3000KM = [550,650,750,800,700]
PRECIO_ADICIONAL_DESDE_3000KM =[600,700,800,900,800]
COSTOS_MANTENIMIENTO =[0.5 , 1.1, 2, 2.5,2.8]

#Codigo de los vehiculos
#1  = Chico
#2 = Mediano
#3 = Grande
#4 = Camioneta4x4
#5 = Van

#Datos generados
KM_Chico = []
KM_Mediano = []
KM_Grande = []
KM_Camioneta4X4= []
KM_Van = []
#Costos  km*costo
Costo_Chico = [ ]
Costo_Mediano = []
Costo_Grande = []
Costo_Camioneta4x4 = []
Costo_Van = []
#FACTURACIÓN
Facturacion_Chico = []
Facturacion_Mediano =[]
Facturacion_Grande =[]
Facturacion_Camioneta4x4 =[]
Facturacion_Van =[]

#GENERACION DE CLIENTES CON LOS KM'S
def generar_km(listaVehiculo):
    num_clientes = random.randint(MIN_CLIENTES//5,MAX_CLIENTES//5)
    for i in range(num_clientes):
        km_recorridos = random.randint(MIN_KM, MAX_KM)
        listaVehiculo.append(km_recorridos)

def generar_datos(Chico, Mediano, Grande, Camioneta, Van):
        #num_clientes = random.randint(MIN_CLIENTES,MAX_CLIENTES)
    generar_km(Chico)
    generar_km(Mediano)
    generar_km(Grande)
    generar_km(Camioneta)
    generar_km(Van)

#GENERACION DE COSTOS DEPENDIENDO DEL VEHICULO
def generar_costo(lista,tipoDeVehiculo):
    for i in range(len(lista)):
        costo = lista[i] * COSTOS_MANTENIMIENTO[tipoDeVehiculo-1]
        if(tipoDeVehiculo==1):
            Costo_Chico.append(costo)
        elif (tipoDeVehiculo==2):
            Costo_Mediano.append(costo)
        elif(tipoDeVehiculo==3):
            Costo_Grande.append(costo)
        elif(tipoDeVehiculo==4):
            Costo_Camioneta4x4.append(costo)
        else: 
            Costo_Van.append(costo)

def generar_costos_vehiculos(Chico, Mediano, Grande, Camioneta, Van):
    generar_costo(Chico,1)
    generar_costo(Mediano,2)
    generar_costo(Grande,3)
    generar_costo(Camioneta,4)
    generar_costo(Van,5)

# GENERACION DE FACTURACIÓN DEPENDIENDO DEL VEHICULO
def generar_facturacion(lista, tipoDeVehiculo):
    for km_recorridos in lista:
        precio_1000 = PRECIO_FIJO_HASTA_1000KM[tipoDeVehiculo-1]
        precio_adicional_antes_3000 = PRECIO_ADICIONAL_HASTA_3000KM[tipoDeVehiculo-1]
        precio_adicional_despues_3000 = PRECIO_ADICIONAL_DESDE_3000KM[tipoDeVehiculo-1]
        if km_recorridos <= 1000:
            facturacion = precio_1000
        elif km_recorridos <= 3000:
            km_despues_1000 = km_recorridos - 1000
            facturacion = precio_1000 + (km_despues_1000 * precio_adicional_antes_3000)
        else:
            km_despues_3000 = km_recorridos - 3000
            facturacion = precio_1000 + (2000 * precio_adicional_antes_3000) + (km_despues_3000 * precio_adicional_despues_3000)

        if(tipoDeVehiculo == 1):
            Facturacion_Chico.append(facturacion)
        elif (tipoDeVehiculo == 2):
            Facturacion_Mediano.append(facturacion)
        elif(tipoDeVehiculo == 3):
            Facturacion_Grande.append(facturacion)
        elif(tipoDeVehiculo == 4):
            Facturacion_Camioneta4x4.append(facturacion)
        else:
            Facturacion_Van.append(facturacion)

def generar_datos_facturacion(Chico, Mediano, Grande, Camioneta, Van):
    generar_facturacion(Chico, 1)
    generar_facturacion(Mediano, 2)
    generar_facturacion(Grande, 3)
    generar_facturacion(Camioneta, 4)
    generar_facturacion(Van, 5)

# TOTAL DE LA FACTURACIÓN DEL MES
def facturacion_total():
    total = 0
    for facturacion in Facturacion_Chico:
        total += facturacion
    for facturacion in Facturacion_Mediano:
        total += facturacion
    for facturacion in Facturacion_Grande:
        total += facturacion
    for facturacion in Facturacion_Camioneta4x4:
        total += facturacion
    for facturacion in Facturacion_Van:
        total += facturacion
    return total


#MENÚ PRINCIPAL
# print("TAMAÑO DE VECTOR 1", len(KM_Chico))
# print("TAMAÑO DE VECTOR 2", len(KM_Mediano))
# print("TAMAÑO DE VECTOR 3", len(KM_Grande))
# print("TAMAÑO DE VECTOR 4", len(KM_Camioneta4X4))
# print("TAMAÑO DE VECTOR 5", len(KM_Van))

# print("km de chico 1", KM_Chico[0])

# print("km de chico 2", KM_Chico[1])

# print("km de chico 3", KM_Chico[2])

# for i in range(len(Costo_Chico)):
#     print(Costo_Chico[i])


# Menú principal
generar_datos(KM_Chico, KM_Mediano, KM_Grande, KM_Camioneta4X4, KM_Van)
generar_costos_vehiculos(KM_Chico, KM_Mediano, KM_Grande, KM_Camioneta4X4, KM_Van)
generar_datos_facturacion()
Bandera = True

print("km de chico 1", KM_Chico[0])
print("Tamaño de chico ", len(Costo_Chico))
print("facturacion de vehiculo 1: ", KM_Chico[0])
for i in range(len(Costo_Chico)):
    print(Costo_Chico[i])
print("\n" * 5)

print("km de mediano 1", KM_Mediano[0])
print("Tamaño de mediano ", len(Costo_Mediano))
for i in range(len(Costo_Mediano)):
    print(Costo_Mediano[i])
print("\n" * 5)

print("km de grande 1", KM_Grande[0])
print("Tamaño de grande ", len(Costo_Grande))
for i in range(len(Costo_Grande)):
    print(Costo_Grande[i])
print("\n" * 5)

print("km de 4x4 1", KM_Camioneta4X4[0])
print("Tamaño de 4x4 ", len(Costo_Camioneta4x4))
for i in range(len(Costo_Camioneta4x4)):
    print(Costo_Camioneta4x4[i])
print("\n" * 5)

print("km de Van 1", KM_Van[0])
print("Tamaño de van ", len(Costo_Van))
for i in range(len(Costo_Van)):
    print(Costo_Van[i])
print("\n" * 6)

while Bandera:
    print("MENU PRINCIPAL")
    print("1. Facturación total del mes")
    print("2. Facturación por tipo de vehículo")
    print("3. Lista detallada de facturación para cada cliente")
    print("4. Filtrar por tipo de vehículo")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("\nHa seleccionado Facturación total del mes")
        # Aquí puedes agregar la lógica para la opción 1
        input("Presione Enter para continuar...")
        print("\n" * 100)
    elif opcion == '2':
        print("\nHa seleccionado Facturación por tipo de vehículo")
        # Aquí puedes agregar la lógica para la opción 2
        input("Presione Enter para continuar...")
        print("\n" * 100)
    elif opcion == '3':
        print("\nHa seleccionado Lista detallada de facturación para cada cliente")
        # Aquí puedes agregar la lógica para la opción 3
        input("Presione Enter para continuar...")
        print("\n" * 100)
    elif opcion == '4':
        print("\nHa seleccionado Filtrar por tipo de vehículo")
        # Aquí puedes agregar la lógica para la opción 4
        input("Presione Enter para continuar...")
        print("\n" * 100)
    elif opcion == '5':
        print("\nSaliendo del programa...")
        Bandera = False
    else:
        print("\nSeleccione una opción válida")
        input("Presione Enter para continuar...")
        print("\n" * 100)
print("Gracias por utilizar el programa.")