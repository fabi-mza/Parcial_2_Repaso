# El Inventario del Club de Lectura
# Nuestra base de datos en memoria (empieza vacía)
biblioteca = []

def menu_principal():
        print("\n=== MENU CLUB DE LECTURA ===")
        print("1. Carga inicial de libros")
        print("2. Ver catálogo completo")
        print("3. Buscar un libro")
        print("4. Ver alerta de libros agotados")
        print("5. Sumar un título nuevo")
        print("6. Prestar o devolver un libro")
        print("7. Salir de la biblioteca")

# Herramienta para pedir números sin que el programa "explote" si escriben texto
def pedir_entero(mensaje):
    while True:
        try:
            valor = input(mensaje)
            return int(valor)
        except ValueError:
            print("Error: Debe ingresar un número entero.")

# Herramienta para buscar un libro por su nombre sin importar mayúsculas/minúsculas
def buscar_libro_por_titulo(titulo_buscado):
    for libro in biblioteca:
        # Usamos .strip() para sacar espacios y .upper() para ignorar mayúsculas
        if libro['titulo'].strip().upper() == titulo_buscado.strip().upper():
            return libro  # Si lo encuentra, devuelve el diccionario entero del libro
    return None  # Si termina el ciclo y no encontró nada, devuelve None


def agregar_nuevo_libro():
    print("\n--- Sumar un Título Nuevo ---")
    # Pedimos el título y limpiamos espacios rebeldes
    titulo = input("Ingresá el título del libro: ").strip()
    
    # Validación 1: si esta vacio
    if not titulo:
        print("Error: El título del libro no puede estar completamente vacío.")
        return # El 'return' vacío corta la función acá y no sigue ejecutando lo de abajo
        
    # Validación 2: si ya existe
    if buscar_libro_por_titulo(titulo):
        print(f"Error: El libro '{titulo}' ya está registrado en el catálogo.")
        return 
        
    # Validación 3: Copias negativas
    copias = pedir_entero("Ingresá la cantidad de copias disponibles: ")
    if copias < 0:
        print("Error: No podés registrar una cantidad negativa de copias.")
        return 

    # Si llegó hasta acá, significa que pasó todos los "if" anteriores sin salir
    nuevo_libro = {
        'titulo': titulo,
        'copias': copias
    }
    biblioteca.append(nuevo_libro)
    print(f"'{titulo}' se guardó correctamente.")


def carga_inicial():
    print("\n--- Carga Inicial del Club ---")
    cantidad = pedir_entero("¿Cuántos libros desea cargar?: ")

    if cantidad <= 0:
        print("Cantidad no válida. Volviendo al menú.")
        return # Corta la función acá y vuelve al menú

    for i in range(cantidad):
        print(f"\n-> Cargando libro {i + 1} de {cantidad}:")
        agregar_nuevo_libro()

def ver_catalogo():
    print("\n--- Catálogo de Libros ---")
    
    # Si la lista está vacía
    if not biblioteca:
        print("Aún no hay libros registrados en la biblioteca.")
        return
        
    # Si tiene datos, la recorremos con un for
    for libro in biblioteca:
        print(f"{libro['titulo']} | Copias: {libro['copias']}")

def buscar_libro():
    print("\n--- Buscador de Títulos ---")
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
        
    busqueda = input("¿Qué libro estás buscando?: ")
    encontrado = buscar_libro_por_titulo(busqueda)
    
    if encontrado:
        print(f"Libro disponible. Quedan {encontrado['copias']} copias de '{encontrado['titulo']}'.")
    else:
        print(f"Lo sentimos, no tenemos ningún libro que se llame '{busqueda}'.")

def alerta_agotados():
    print("\n--- Alerta de Libros Sin Stock ---")
    hubo_agotados = False
    
    for libro in biblioteca:
        if libro['copias'] == 0:
            print(f"REPONER: '{libro['titulo']}' no tiene copias disponibles.")
            hubo_agotados = True
            
    if not hubo_agotados:
        print("No hay ningún libro agotado.")

def prestar_o_devolver():
    print("\n--- Préstamos y Devoluciones ---")
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
        
    titulo = input("Ingresá el título del libro a modificar: ")
    libro = buscar_libro_por_titulo(titulo)
    
    if not libro:
        print(f"El libro '{titulo}' no existe en el registro.")
        return
        
    print(f"Libro: '{libro['titulo']}' | Copias actuales: {libro['copias']}")
    print("1 - Prestar (restar 1 copia)")
    print("2 - Devolver (sumar 1 copia)")
    opcion_cambio = input("¿Qué operación querés hacer?: ").strip()
    
    try:
        match opcion_cambio:
            case '1':
                if libro['copias'] <= 0:
                    raise ValueError("No se puede prestar este libro porque ya tiene 0 copias.")
                libro['copias'] -= 1
                print("Préstamo concedido con éxito.")
            case '2':
                libro['copias'] += 1
                print("Devolución registrada con éxito.")
            case _:
                print("Opción inválida. Operación cancelada.")
                
    except ValueError as error_actualizacion:
        print(f"Operación cancelada: {error_actualizacion}")