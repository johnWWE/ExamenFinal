'''
Crea un programa en Python que simule una lista de compras. El programa debe permitir al usuario agregar
productos al final de la lista, eliminar productos del inicio de la lista y mostrar todos los productos
en la lista en orden de compra.'''

# Creamos una clase Nodo para representar cada elemento de la lista de compras
class Nodo:
    def __init__(self, dato):
        self.dato = dato                        # El dato que queremos almacenar en el nodo
        self.siguiente = None               # Es unaa Referencia al siguiente nodo de la lista

# Creamos una clase para representar la lista de compras
class ListaDeCompras:
    def __init__(self):
        self.cabeza = None   # Es la referencia al primer nodo de la lista (cabeza)
        self.cola = None     # Es la Referencia al último nodo de la lista (cola)

    # Función para agregar un producto al final de nuestra lista creeda con anterioridad
    def agregar_producto(self, producto):
        nuevo_nodo = Nodo(producto)   # Creamos un nuevo nodo con el producto
        if not self.cabeza:             # Si la lista está vacía, el nuevo nodo es la cabeza y la cola
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:                           # Si la lista no está vacía, agregamos el nuevo nodo al final y actualizamos la cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    # Función para eliminar el primer producto de la lista
    def eliminar_producto(self):
        if not self.cabeza:   # Si la lista está vacía, no hacemos nada
            print("La lista de compras está vacía.")
            return
        self.cabeza = self.cabeza.siguiente   # Actualizamos la cabeza para eliminar el primer nodo

    # Función para mostrar la lista de compras
    def mostrar_lista(self):
        if not self.cabeza:   # Si la lista está vacía, no hay productos que mostrar
            print("La lista de compras está vacía.")
            return
        nodo_actual = self.cabeza   # Empezamos por la cabeza de la lista
        while nodo_actual:   # Recorremos la lista desde la cabeza hasta la cola
            print(nodo_actual.dato)   # Imprimimos el dato del nodo actual
            nodo_actual = nodo_actual.siguiente   # Pasamos al siguiente nodo

# Creamos una instancia de la lista de compras
lista_de_compras = ListaDeCompras()

# nuestro menu principal
while True:
    # Mostramos el menú de opciones
    print("Bienvenido a la lista de compras")
    print("[1.] Agregar producto | ")
    print("[2.]Eliminar producto |")
    print("[3.] Mostrar lista de compras | ")
    print("[0] Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        # agregando el nombre del producto
        producto = input("Ingrese el nombre del producto: ")
        lista_de_compras.agregar_producto(producto)
        print(f"{producto} ha sido agregado a la lista de compras.")
    elif opcion == 2:
        # Si el usuario elige la opción 2, eliminamos el primer producto de la lista, no importaa cuntos haya
        lista_de_compras.eliminar_producto()
        print("El primer producto de la lista ha sido eliminado.")
    elif opcion == 3:
        print("Mostraando la Lista de compras: ")
        lista_de_compras.mostrar_lista()
    elif opcion ==0:
        print('Gracias por usar nuestros servivios')
        print('....finalizando el prograama......')
        break
    else:
        print("Opcion incorrecta, Intente de nuevo por favor")
