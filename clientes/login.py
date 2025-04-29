from clientes.cliente import (
    Cliente,
)  # Importamos la clase Cliente para poder usarla en el Signup/Login

usuarios = {}
usuarios_bloqueados = set()
clientes = {}  # Para guardar objetos Cliente asociados al usuario


def sign_up():
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    while nombre_usuario in usuarios:
        nombre_usuario = input(
            "El nombre ya existe. Ingrese un nombre de usuario válido: "
        )

    contraseña = input("Ingrese una contraseña: ")
    while len(contraseña) < 8 or len(contraseña) > 12:
        print("La contraseña debe tener entre 8 y 12 caracteres.")
        contraseña = input("Ingrese una contraseña válida: ")

    usuarios[nombre_usuario] = contraseña
    print(f"Usuario '{nombre_usuario}' registrado exitosamente.")

    # Pedimos los datos del cliente
    print(f"Ingreso de datos para el usuario '{nombre_usuario}':")
    nombre_cliente = input("Nombre completo: ")
    email_cliente = input("Email: ")
    direccion_cliente = input("Dirección: ")
    telefono_cliente = input("Teléfono: ")

    # Creamos el objeto Cliente y lo guardamos en el diccionario clientes{}
    cliente_nuevo = Cliente(
        nombre_cliente, email_cliente, direccion_cliente, telefono_cliente
    )
    clientes[nombre_usuario] = cliente_nuevo


def datos_usuarios():
    print("<---- Datos de los usuarios en la base ---->")
    for usuario in usuarios:
        print(f"Usuario: {usuario} | Contraseña: {usuarios[usuario]}")
        if usuario in clientes:
            print("Información del Cliente asociado:")
            print(clientes[usuario].mostrar_informacion())
            print("-" * 30)


def login():
    loginuser = input("Ingrese el usuario: ")
    while loginuser not in usuarios:
        loginuser = input("Usuario inexistente. Ingrese un usuario válido: ")
    if loginuser in usuarios_bloqueados:
        print(f"El usuario '{loginuser}' está BLOQUEADO. No puede iniciar sesión.")
        return None
    intentos = 0
    max_intentos = 3
    while intentos < max_intentos:
        password = input("Ingrese la contraseña del usuario: ")
        if password == usuarios[loginuser]:
            print(f"Contraseña correcta - Bienvenido, {clientes[loginuser].nombre}!")
            return loginuser  # Retorna el nombre de usuario
        else:
            intentos += 1
            print("Contraseña incorrecta.")
    print(f"Demasiados intentos fallidos. El usuario '{loginuser}' ha sido BLOQUEADO.")
    usuarios_bloqueados.add(loginuser)
    return None
