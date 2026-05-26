from club_lectura_fn import *

while True:
    menu_principal()
        
    opcion = input("Elegí una opción (1-7): ").strip()
        
    match opcion:
        case '1':
            carga_inicial()
        case '2':
            ver_catalogo()
        case '3':
            buscar_libro()
        case '4':
            alerta_agotados()
        case '5':
            agregar_nuevo_libro()
        case '6':
            prestar_o_devolver()
        case '7':
            print("\nSaliendo del sistema gracias por usar nuestro servicio.")
            break # Rompe el ciclo while y cierra el programa
        case _:
            print("Error. Debe ingresar un número del 1 al 7.")