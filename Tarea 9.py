# Lista global para almacenar los libros
biblioteca = []

def agregar_libros(*titulos):
    for titulo in titulos:
        if any(libro["titulo"].lower() == titulo.lower() for libro in biblioteca):
            print(f"El libro '{titulo}' ya existe en la biblioteca.")
            continue
        libro = {"titulo": titulo, "autor": None, "genero": None, "año": None}
        biblioteca.append(libro)
        print(f"Libro '{titulo}' agregado correctamente.")


def asignar_detalles(titulo, autor, genero, año):
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            libro["autor"] = autor
            libro["genero"] = genero
            libro["año"] = año
            print(f"Detalles asignados a '{titulo}'.")
            return
    print(f"El libro '{titulo}' no se encontró en la biblioteca.")


def mostrar_biblioteca():
    if not biblioteca:
        print("La biblioteca está vacía.")
        return

    print("\n=== LISTA DE LIBROS ===")
    for i, libro in enumerate(biblioteca, 1):
        print(f"\nLibro {i}:")
        print(f"  Título: {libro['titulo']}")
        print(f"  Autor:  {libro['autor']}")
        print(f"  Género: {libro['genero']}")
        print(f"  Año:    {libro['año']}")


def buscar_libros(**filtros):
    resultados = biblioteca

    if "genero" in filtros:
        resultados = [libro for libro in resultados if libro["genero"] and libro["genero"].lower() == filtros["genero"].lower()]

    if "autor" in filtros:
        resultados = [libro for libro in resultados if libro["autor"] and libro["autor"].lower() == filtros["autor"].lower()]

    if "año_max" in filtros:
        resultados = [libro for libro in resultados if libro["año"] is not None and libro["año"] <= filtros["año_max"]]

    if resultados:
        print("\n=== RESULTADOS DE LA BÚSQUEDA ===")
        for libro in resultados:
            print(f"Título: {libro['titulo']} | Autor: {libro['autor']} | Género: {libro['genero']} | Año: {libro['año']}")
    else:
        print("No se encontraron libros con esos filtros.")


# Menú interactivo
def menu():
    while True:
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Agregar libros")
        print("2. Asignar detalles a un libro")
        print("3. Mostrar biblioteca")
        print("4. Buscar libros")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulos = input("Ingrese los títulos separados por coma: ").split(",")
            titulos = [t.strip() for t in titulos]
            agregar_libros(*titulos)

        elif opcion == "2":
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            año = int(input("Año: "))
            asignar_detalles(titulo, autor, genero, año)

        elif opcion == "3":
            mostrar_biblioteca()

        elif opcion == "4":
            genero = input("Filtrar por género (Enter para omitir): ").strip() or None
            autor = input("Filtrar por autor (Enter para omitir): ").strip() or None
            año_max = input("Filtrar por año máximo (Enter para omitir): ").strip()
            año_max = int(año_max) if año_max else None

            filtros = {}
            if genero: filtros["genero"] = genero
            if autor: filtros["autor"] = autor
            if año_max is not None: filtros["año_max"] = año_max

            buscar_libros(**filtros)

        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")


# Ejecutar menú
menu()