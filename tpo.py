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
# VEHICULOS = ["CHICO", "MEDIANO", "GRANDE", "CAMIONETA 4X4", "VAN"]
MIN_CLIENTES = 200
MAX_CLIENTES = 450
MIN_KM = 100
MAX_KM = 5000
PRECIO_FIJO_HASTA_100KM = [7500, 8500,9500,10000,12000]
PRECIO_ADICIONAL_HASTA_3000KM = [550,650,750,800,700]
PRECIO_ADICIONAL_DESDE_3000KM =[600,700,800,900,800]

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

#Facturacion
Facturacion_chico = []
Facturacion_Mediano =[]


# Costos definidos por tipo de vehículo
def obtener_costos(tipo_vehiculo):
    if tipo_vehiculo == "CHICO":
        return 0.5, 7500, 550, 600
    elif tipo_vehiculo == "MEDIANO":
        return 1.1, 8500, 650, 700
    elif tipo_vehiculo == "GRANDE":
        return 2, 9500, 750 , 800
    elif tipo_vehiculo == "CAMIONETA 4X4":
        return 2.5, 10000, 800, 900
    elif tipo_vehiculo == "VAN":    
        return 2.8, 12000, 700, 800

# # Generar datos aleatorios para los clientes
# def generar_datos():
#     num_clientes = random.randint(MIN_CLIENTES, MAX_CLIENTES)
#     clientes = []
#     for i in range(num_clientes):
#         tipo_vehiculo = VEHICULOS[random.randint(0, len(VEHICULOS) - 1)]
#         km_recorridos = random.randint(MIN_KM, MAX_KM)
#         clientes.append({"tipo_vehiculo": tipo_vehiculo, "km_recorridos": km_recorridos})
#     return clientes

def generar_km(listaVehiculo, numeroClientes):
    for i in range(numeroClientes):
        km_recorridos = random.randint(MIN_KM, MAX_KM)
        listaVehiculo.append(km_recorridos)
       

def generar_datos(chico, mediano, grande, camioneta, van):
    num_clientes = random.randint(MIN_CLIENTES,MAX_CLIENTES)

    generar_km(chico, num_clientes)
    generar_km(mediano, num_clientes)
    generar_km(grande, num_clientes)
    generar_km(camioneta, num_clientes)
    generar_km(van, num_clientes)
  



# Calcular la facturación total de un cliente
def calcular_facturacion(tipo_vehiculo, km_recorridos):
    costo_mantenimiento, precio_1000, precio_adicional_antes_3000, precio_adicional_despues_3000 = obtener_costos(tipo_vehiculo)
    if km_recorridos <= 1000:
        return precio_1000 + (km_recorridos * costo_mantenimiento)
    elif km_recorridos <= 3000:
        km_despues_1000 = km_recorridos - 1000
        return (1000 * costo_mantenimiento) + (km_despues_1000 * precio_adicional_antes_3000)
    elif km_recorridos > 3000:
        km_extra = km_recorridos - 3000
        return (km_recorridos * costo_mantenimiento) + (precio_adicional_antes_3000 * 2000) + (km_extra * precio_adicional_despues_3000)  

# Total d ela facturación del mes
def facturacion_total(clientes):
    total = 0
    for cliente in clientes:
        total += calcular_facturacion(cliente["tipo_vehiculo"], cliente["km_recorridos"])
    return total

# Menú principal
# def main():


#Podemos usar la función exit, funcions de formato
# no usar funciones que simplifiquen la logica
#funcion de color

generar_datos(KM_Chico, KM_Mediano, KM_Grande, KM_Camioneta4X4,KM_Van)
# for i in range(len(KM_Van)):
#     print(KM_Van[i])


Bandera = True

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



