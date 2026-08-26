def mostrar_menu():
    print("\n===== CAFETERÍA =====")
    print ("\n1. Registrar venta \n2. Reponer inventario \n3. Ver estado \n4. Cerrar cafetería")

def registrar_venta(inventario, dinero, ventas_realizadas, monto):
    if inventario > 0 :
        inventario -= 1
        dinero += monto
        ventas_realizadas += 1
        print("\n¡Venta registrada exitósamente!\n")
        return inventario, dinero, ventas_realizadas
    elif inventario <= 0:
        print("¡Valor invalido!")
    else:
        print("Inventario Vacío")

def reponer_inventario(inventario):
    inventario_actualizado = 0
    inventario_actualizado = int(input("\nCantidad de inventario: "))
    if inventario > 0:
        inventario += inventario_actualizado
        print("¡Inventario Actualizado!")
        return inventario
    else: 
        print("Cantidad inválida")

def consultar_estado(nombre_cafeteria, dinero, inventario, ventas_realizadas):
    print("\n===== ESTADO ACTUAL =====")
    print(f"Cafetería: {nombre_cafeteria}")
    print(f"Dinero Acumulado: {dinero}")
    print(f"Inventario: {inventario}")
    print(f"Ventas: {ventas_realizadas}")

def cerrar_cafeteria():
    print("¡Cerrado! ")
    
def main():
    nombre_cafeteria = input("\nIngrese el nombre de la cafetería: ")
    monto = float(input("Ingrese el monto: "))
    dinero = 0
    ventas_realizadas = 0
    inventario = 50
    
    while (True):
        mostrar_menu()
        opcion = int(input("\nSeleccione la opcion deseada: "))
        match opcion:
           case 1:
              inventario, dinero, ventas_realizadas = registrar_venta(inventario, dinero, ventas_realizadas, monto)
           case 2:
               inventario = reponer_inventario(inventario)
           case 3:
              consultar_estado(nombre_cafeteria, dinero, inventario, ventas_realizadas)
           case 4:
               cerrar_cafeteria()
               break
           case _:
              print("Opción Inválida. Seleccione una opción disponible.")
       
main()