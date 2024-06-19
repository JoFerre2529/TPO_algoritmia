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
VEHICULOS = ["CHICO", "MEDIANO", "GRANDE", "CAMIONETA 4X4", "VAN"]
MIN_CLIENTES = 200
MAX_CLIENTES = 450
MIN_KM = 100
MAX_KM = 5000

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

# Generar datos aleatorios para los clientes
def generar_datos():
    num_clientes = random.randint(MIN_CLIENTES, MAX_CLIENTES)
    clientes = []
    for _ in range(num_clientes):
        tipo_vehiculo = VEHICULOS[random.randint(0, len(VEHICULOS) - 1)]
        km_recorridos = random.randint(MIN_KM, MAX_KM)
        clientes.append({"tipo_vehiculo": tipo_vehiculo, "km_recorridos": km_recorridos})
    return clientes

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
def main():
    clientes = generar_datos()
    while True:
        print("\nMenú:")
        print("1. Facturación total del mes")
        print("2. Facturación por tipo de vehículo")
        print("3. Lista detallada de facturación para cada cliente")
        print("4. Filtrar por tipo de vehículo")
        print("5. Salir")
        opcion = input("Elija una opción: ")