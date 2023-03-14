from paquete.cliente import *
import random

cliente1 = Cliente("Juan", "juan@gmail.com", "San Martín 123")
cliente2 = Cliente("Romina", "romina@hotmail.com", "Reconquista 300")

cliente1.realizar_compra(random.randint(1, 10))
cliente2.realizar_compra(random.randint(1, 10))

cliente1.realizar_compra(random.randint(1, 10))
cliente2.realizar_compra(random.randint(1, 10))

cliente1.realizar_compra(random.randint(1, 10))
cliente2.realizar_compra(random.randint(1, 10))

if(cliente1.cantidad_comprada > cliente2.cantidad_comprada):
    print(f"El cliente {cliente1.nombre} es el mayor comprador")
elif(cliente1.cantidad_comprada < cliente2.cantidad_comprada):
    print(f"El cliente {cliente2.nombre} es el mayor comprador")
else:
    print("Ambos clientes compraron la misma cantidad")

print(f"El primer cliente se llamaba {cliente1.nombre}")
cliente1.actualizar_datos("Miguel", None, None)
print(f"El primer cliente ahora se llama {cliente1.nombre}")

print(cliente1);