class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}"

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"La dirección de {self.nombre} ha sido actualizada.")
    
    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"La direccion de correo de {self.nombre} ha sido actualizada.")

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print(f"El numero telefonico de {self.nombre} ha sido actualizado.")

    def mostrar_informacion(self):
        info = (
            f"Nombre: {self.nombre}\n"
            f"Email: {self.email}\n"
            f"Dirección: {self.direccion}\n"
            f"Teléfono: {self.telefono}\n"
        )
        return info