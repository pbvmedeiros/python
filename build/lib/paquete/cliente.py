class Cliente:
    def __init__(self, nombre, correo, direccion):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.cantidad_comprada = 0

    def realizar_compra(self, unidades):
        self.cantidad_comprada += unidades
        print(f"{self.nombre} compró {unidades} unidad(es). Ya lleva comprada(s) {self.cantidad_comprada}.")

    def actualizar_datos(self, nombre=None, correo=None, direccion=None):
        if nombre:
            self.nombre = nombre
        if correo:
            self.correo = correo
        if direccion:
            self.direccion = direccion
        
    def __str__(self):
        return f"Cliente: {self.nombre}"
