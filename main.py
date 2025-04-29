from clientes.login import login, sign_up, datos_usuarios, clientes


def menu_compras(usuario):
    cliente = clientes[usuario]
    while True:
        print("\n--- Menú de Compras ---")
        print("1. Ver información del cliente")
        print("2. Comprar producto")
        print("3. Ver historial de compras (próxima implementación)")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(cliente.mostrar_informacion())
        elif opcion == "2":
            producto = input("Ingrese el producto que desea comprar: ")
            print(f"{cliente.nombre} ha comprado {producto}. ¡Gracias por su compra!")
        elif opcion == "3":
            print("Historial de compras: Funcionalidad en desarrollo.")
        elif opcion == "4":
            print(f"Hasta luego, {cliente.nombre}!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def main():
    while True:
        print("\n--- Bienvenido al sistema ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Mostrar usuarios")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sign_up()
        elif opcion == "2":
            usuario = login()
            if usuario:
                menu_compras(usuario)
        elif opcion == "3":
            datos_usuarios()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
