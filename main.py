from logica import agregar_compositor, agregar_director, agregar_interprete, agregar_obra, listar_obras

def main():
    while True:
        print("\n1. Agregar Compositor")
        print("2. Agregar Director")
        print("3. Agregar Intérprete")
        print("4. Agregar Obra")
        print("5. Listar Obras")
        print("6. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del compositor: ")
            agregar_compositor(nombre)
            print("Compositor agregado exitosamente.")
        elif opcion == '2':
            nombre = input("Ingrese el nombre del director: ")
            agregar_director(nombre)
            print("Director agregado exitosamente.")
        elif opcion == '3':
            nombre = input("Ingrese el nombre del intérprete: ")
            instrumento = input("Ingrese el instrumento: ")
            agregar_interprete(nombre, instrumento)
            print("Intérprete agregado exitosamente.")
        elif opcion == '4':
            titulo = input("Ingrese el título de la obra: ")
            compositor_id = int(input("Ingrese el ID del compositor: "))
            director_id = int(input("Ingrese el ID del director: "))
            interprete_id = int(input("Ingrese el ID del intérprete: "))
            agregar_obra(titulo, compositor_id, director_id, interprete_id)
            print("Obra agregada exitosamente.")
        elif opcion == '5':
            print("\nListado de Obras:")
            obras = listar_obras()
            for obra in obras:
                print(f"Título: {obra.titulo}, Compositor: {obra.compositor.nombre}, Director: {obra.director.nombre}, Intérprete: {obra.interprete.nombre}")
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
