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
#CONSTANTES

#VEHICULOS = ["Chico", "Mediano", "Grande", "Camioneta 4x4", "Van"]
MIN_CLIENTES = 200
MAX_CLIENTES = 450
MIN_KM = 100
MAX_KM = 5000
PRECIO_FIJO_HASTA_1000KM = [7500, 8500, 9500, 10000, 12000]
PRECIO_ADICIONAL_HASTA_3000KM = [550, 650, 750, 800, 700]
PRECIO_ADICIONAL_DESDE_3000KM =[600, 700, 800, 900, 800]
COSTOS_MANTENIMIENTO =[0.5, 1.1, 2, 2.5, 2.8]

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


#/////////////// GENERACIÓN DE DATOS ///////////////

#GENERACION DE CLIENTES CON LOS KM'S
def generar_km(listaVehiculo):
    num_clientes = random.randint(MIN_CLIENTES//5,MAX_CLIENTES//5)
    for i in range(num_clientes):
        km_recorridos = random.randint(MIN_KM, MAX_KM)
        listaVehiculo.append(km_recorridos)

def generar_datos_KM(Chico, Mediano, Grande, Camioneta, Van):
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
    for i in range(len(lista)):
        km_recorridos = lista[i]

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

#/////////////CALCULOS DE FACTURACION ////////////

# TOTAL DE LA FACTURACIÓN DEL MES
def calcular_facturacion_total():
    total = 0

    total += calcular_facturacion_chico()
    total += calcular_facturacion_mediano()
    total += calcular_facturacion_grande()
    total += calcular_facturacion_camioneta()
    total += calcular_facturacion_van()

    redondeo = round(total,2)

    return redondeo

#FACTURACION POR CADA TIPO DE VEHICULO
def calcular_facturacion_chico():
    total = 0
    for i in range(len(Facturacion_Chico)) :
        total += Facturacion_Chico[i]
    return total

def calcular_facturacion_mediano():
    total = 0
    for i in range(len(Facturacion_Mediano)):
        total += Facturacion_Mediano[i]
    return total

def calcular_facturacion_grande():
    total = 0
    for i in range(len(Facturacion_Grande)):
        total += Facturacion_Grande[i]
    return total

def calcular_facturacion_camioneta():
    total = 0
    for i in range(len(Facturacion_Camioneta4x4)):
        total += Facturacion_Camioneta4x4[i]
    return total
    
def calcular_facturacion_van():
    total = 0
    for i in range(len(Facturacion_Van)):
        total += Facturacion_Van[i]
    return total

#CALCULO DE TOTAL DE QUILOMETROS POR CADA VEHICULO

def calcular_km_chico():
    total = 0
    for km in range(len(KM_Chico)):
        total += km
    return total

def calcular_km_mediano():
    total = 0
    for km in range(len(KM_Mediano)):
        total += km
    return total

def calcular_km_grande():
    total = 0
    for km in range(len(KM_Grande)):
        total += km
    return total

def calcular_km_camioneta():
    total = 0
    for km in range(len(KM_Camioneta4X4)):
        total += km
    return total
    
def calcular_km_van():
    total = 0
    for km in range(len(KM_Van)):
        total += km
    return total



#FUNCIONES DE COSTO POR CADA TIPO 


def  calcular_costo_chico():
    total = 0
    for i in range(len(Costo_Chico)):
        total += Costo_Chico[i]
     
        return  round(total,2)

def  calcular_costo_mediano():
    total = 0
    for i in range(len(Costo_Mediano)):
        total += Costo_Mediano[i]
        return  round(total,2)

def  calcular_costo_grande():
    total = 0
    for i in range(len(Costo_Grande)):
        total += Costo_Grande[i]
        return  round(total,2)

def calcular_costo_camioneta():
    total = 0
    for i in range(len(Costo_Camioneta4x4) ):
        total += Costo_Camioneta4x4[i]
        return total

def  calcular_costo_van():
    total = 0
    for i in range((len(Costo_Van))):
        total += Costo_Van[i]
        return total



def calcular_costo_total():

    total = 0

    total += calcular_costo_chico()
    total += calcular_costo_mediano()
    total += calcular_costo_grande()
    total += calcular_costo_camioneta()
    total += calcular_costo_van()

    redondeo = round(total,2)

    return redondeo

def cantidad_vehiculos():
    cantidad = 0

    cantidad += len(KM_Chico)
    cantidad += len(KM_Mediano)
    cantidad += len(KM_Grande)
    cantidad += len(KM_Camioneta4X4)
    cantidad += len(KM_Van)
    
    return cantidad

# def ordenar(lista_facturacion, lista_km, lista_tipos, lista_costos):
#     largo = len(lista_facturacion)
#     for i in range(largo-1):
#         for j in range(i+1, largo):
#             if (lista_facturacion[i] > lista_facturacion[j]):
#                 aux = lista_facturacion[i]
#                 lista_facturacion[i] = lista_facturacion[j]
#                 lista_facturacion[j] = aux

#                 aux_km = lista_km[i]
#                 lista_km[i] = lista_km[j]
#                 lista_km[j] = aux_km

#                 aux_tipo = lista_tipos[i]
#                 lista_tipos[i] = lista_tipos[j]
#                 lista_tipos[j] = aux_tipo

#                 aux_costos = lista_costos[i]
#                 lista_costos[i] = lista_costos[j]
#                 lista_costos[j] = aux_costos

def ordenar(lista_facturacion, lista_km, lista_tipos, lista_costos):
    largo = len(lista_facturacion)
    for i in range(largo-1):
        for j in range(i+1, largo):
            if (lista_facturacion[i] < lista_facturacion[j]):  
                aux = lista_facturacion[i]
                lista_facturacion[i] = lista_facturacion[j]
                lista_facturacion[j] = aux

                aux_km = lista_km[i]
                lista_km[i] = lista_km[j]
                lista_km[j] = aux_km

                aux_tipo = lista_tipos[i]
                lista_tipos[i] = lista_tipos[j]
                lista_tipos[j] = aux_tipo

                aux_costos = lista_costos[i]
                lista_costos[i] = lista_costos[j]
                lista_costos[j] = aux_costos


#//////////////////EJERCICIOS//////////////////////
def punto_1():
    print("\n")
    print("FACTURACIÓN TOTAL DEL MES  :   $", calcular_facturacion_total())
    print("\n")    
    print("COSTO TOTAL DEL MES  :   $", calcular_costo_total())
    print("\n")
    print("CANTIDAD TOTAL DE VEHICULOS  ", cantidad_vehiculos(), "Unidades")
    print("\n")

# Total de facturación por tipo de vehículo, la cantidad de KM, el costo asociado ordenado por facturación.
def punto_2():
    facturacion_por_tipo = [
        calcular_facturacion_chico(),
        calcular_facturacion_mediano(),
        calcular_facturacion_grande(),
        calcular_facturacion_camioneta(),
        calcular_facturacion_van()
    ]

    km_por_tipo = [
        calcular_km_chico(),
        calcular_km_mediano(),
        calcular_km_grande(),
        calcular_km_camioneta(),
        calcular_km_van()
    ]

    costo_por_tipo = [
        calcular_costo_chico(),
        calcular_costo_mediano(),
        calcular_costo_grande(),
        calcular_costo_camioneta(),
        calcular_costo_van()
    ]

    tipo_vehiculos = [
        "Chico", 
        "Mediano", 
        "Grande", 
        "Camioneta 4x4", 
        "Van"
    ]

    ordenar(facturacion_por_tipo, km_por_tipo, costo_por_tipo, tipo_vehiculos)

    for i in range(len(tipo_vehiculos)):
        print("TIPO DE VEHICULO: ", tipo_vehiculos[i])
        print("FACTURACIÓN:  $", facturacion_por_tipo[i])
        print("CANTIDAD DE KM: ", km_por_tipo[i])
        print("COSTO ASOCIADO:  $", costo_por_tipo[i])
        print()
        print("--------------------------------------")

#Listado completo detallado del total facturado de cada cliente con su tipo de vehículo, ordenado facturación.
def punto_3():
    clientes_detalle = []

    def obtener_facturacion_total(cliente):
        return cliente[4]

    # Clientes tipo Chico
    for i in range(len(KM_Chico)):
        cliente = [
            i + 1,
            'Chico',
            KM_Chico[i],
            Costo_Chico[i],
            Facturacion_Chico[i]
        ]
        clientes_detalle.append(cliente)

    # Clientes tipo Mediano
    for i in range(len(KM_Mediano)):
        cliente = [
            i + 1,
            'Mediano',
            KM_Mediano[i],
            Costo_Mediano[i],
            Facturacion_Mediano[i]
        ]
        clientes_detalle.append(cliente)

    # Clientes tipo Grande
    for i in range(len(KM_Grande)):
        cliente = [
            i + 1,
            'Grande',
            KM_Grande[i],
            Costo_Grande[i],
            Facturacion_Grande[i]
        ]
        clientes_detalle.append(cliente)

    #  Clientes tipo Camioneta 4x4
    for i in range(len(KM_Camioneta4X4)):
        cliente = [
            i + 1,
            'Camioneta 4x4',
            KM_Camioneta4X4[i],
            Costo_Camioneta4x4[i],
            Facturacion_Camioneta4x4[i]
        ]
        clientes_detalle.append(cliente)

    # Clientes tipo Van
    for i in range(len(KM_Van)):
        cliente = [
            i + 1,
            'Van',
            KM_Van[i],
            Costo_Van[i],
            Facturacion_Van[i]
        ]
        clientes_detalle.append(cliente)

    n = len(clientes_detalle)
    for i in range(n):
        for j in range(0, n-i-1):
            if obtener_facturacion_total(clientes_detalle[j]) > obtener_facturacion_total(clientes_detalle[j+1]):
                clientes_detalle[j], clientes_detalle[j+1] = clientes_detalle[j+1], clientes_detalle[j]

    for cliente in clientes_detalle:
        print("Cliente:", cliente[0])
        print("Tipo de vehículo:", cliente[0])
        print("KM recorridos:", cliente[0])
        print("Costo de mantenimiento:", cliente[0])
        print("Facturación total:", cliente[0])

# Poder seleccionar un tipo de vehículo y que se detallen la facturación, la cantidad de clientes y el costo del tipo de vehículo seleccionado.
def punto_4():
    #TODO: Mostrar lista tipo de vehiculos, a que numero corresponde cada uno?
    num_tipo = int(input("Ingrese tipo vehiculo: "))
    facturacion = obtener_facturacion_tipo(num_tipo)
    cant_clientes = obtener_cant_clientes_tipo(num_tipo)
    costo = obtener_costo_tipo(num_tipo)

    print("Facturacion: ", facturacion)
    print("Cantidad de clientes: ", cant_clientes)
    print("Costo: ", costo)
    

def obtener_facturacion_tipo(num_tipo):
    if num_tipo == 1:
        return   calcular_facturacion_chico()
    elif num_tipo == 2:
        return   calcular_facturacion_mediano()
    elif num_tipo == 3:
        return   calcular_facturacion_grande()
    elif num_tipo == 4:
        return   calcular_facturacion_camioneta()
    elif num_tipo == 5:
        return   calcular_facturacion_van()

def obtener_cant_clientes_tipo(num_tipo):
    if num_tipo == 1:
        return len(Facturacion_Chico)
    elif num_tipo == 2:
        return len(Facturacion_Mediano)
    elif num_tipo == 3:
        return len(Facturacion_Grande)
    elif num_tipo == 4:
        return len(Facturacion_Camioneta4x4)
    elif num_tipo == 5:
        return len(Facturacion_Van)

def obtener_costo_tipo(num_tipo):
    if num_tipo == 1:
        return len(Costo_Chico)
    elif num_tipo == 2:
        return len(Costo_Mediano)
    elif num_tipo == 3:
        return len(Costo_Grande)
    elif num_tipo == 4:
        return len(Costo_Camioneta4x4)
    elif num_tipo == 5:
        return len(Costo_Van)

# Menú principal
generar_datos_KM(KM_Chico, KM_Mediano, KM_Grande, KM_Camioneta4X4, KM_Van)
generar_costos_vehiculos(KM_Chico, KM_Mediano, KM_Grande, KM_Camioneta4X4, KM_Van)
generar_datos_facturacion(KM_Chico, KM_Mediano, KM_Grande, KM_Camioneta4X4, KM_Van)


Bandera = True

print("km de chico 1", KM_Chico[5])
print("Tamaño de chico ", len(Costo_Chico))
print("costo de chico 1 ", 
      Costo_Chico[5])
print("facturacion de vehiculo 1: ", Facturacion_Chico[5])
            

while Bandera:
    print("============================")
    print("      MENU PRINCIPAL")
    print("============================")
    print("")
    print("1. Facturación total del mes")
    print("2. Facturación por tipo de vehículo")
    print("3. Lista detallada de facturación para cada cliente")
    print("4. Filtrar por tipo de vehículo")
    print("5. Salir")
    print()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        
       
        punto_1()
      
        input("Presione Enter para continuar...")

        print("\n" * 50)
    elif opcion == '2':
      

        punto_2()
        input("Presione Enter para continuar...")
        print("\n" * 50)
    elif opcion == '3':
     
        punto_3()
        input("Presione Enter para continuar...")
        print("\n" * 50)
    elif opcion == '4':
       
     
        punto_4()
        input("Presione Enter para continuar...")
        print("\n" * 50)
    elif opcion == '5':
        print("\nSaliendo del programa...")
        Bandera = False
    else:
        print("\nSeleccione una opción válida")
        input("Presione Enter para continuar...")
        print("\n" * 50)
print("Gracias por utilizar el programa.")





