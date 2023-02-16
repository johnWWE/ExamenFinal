'''
Crea un programa en Python que mantenga un historial de tareas pendientes. El programa debe permitir
al usuario agregar una tarea al inicio de la lista, eliminar una tarea del final de la lista y mostrar todas
las tareas en la lista en orden inverso al que se agregaron. Además, el programa debe contar la cantidad
total de tareas en la lista y mostrar ese número al usuario'''


# Creamos una clase Nodo para representar cada tarea en el historial
class Nodo:
    def __init__(self, tarea, siguiente=None):
        self.tarea = tarea              # El dato que contiene el nodo (la tarea)
        self.siguiente = siguiente         # La referencia al siguiente nodo de la lista

# Creamos una clase para representar el historial en sí
class HistorialTareas:
    def __init__(self):
        self.cabeza = None              # Referencia al primer nodo de la lista (inicialmente vacío)
        self.cola = None                 # Referencia al último nodo de la lista (inicialmente vacío)
        self.numero_tareas = 0          # Cantidad total de tareas en la lista (inicialmente 0)

    def agregar_tarea(self, tarea):
        # Creamos un nuevo nodo con la tarea y lo agregamos al inicio de la lista
        nuevo_nodo = Nodo(tarea, self.cabeza)
        self.cabeza = nuevo_nodo
        # Si la cola está vacía, actualizamos la referencia a la cola
        if not self.cola:
            self.cola = nuevo_nodo
        self.numero_tareas += 1             # Aumentamos la cantidad total de tareas en la lista en 1

    def eliminar_ultima_tarea(self):
        # Si la cabeza está vacía no hacemos nada
        if not self.cabeza:
            return
        # Si la cabeza es el único nodo de la lista, la lista quedará vacía después de eliminarlo
        if not self.cabeza.siguiente:
            self.cabeza = None   # Actualizamos la referencia a la cabeza
            self.cola = None     # Actualizamos la referencia a la cola
            self.numero_tareas = 0  # Actualizamos la cantidad total de tareas en la lista
            return
        # Si la lista tiene más de un nodo, recorremos la lista hasta encontrar el segundo último nodo (antes de la cola)
        actual = self.cabeza
        while actual.siguiente != self.cola:
            actual = actual.siguiente
        # Actualizamos la referencia a la cola y la cantidad total de tareas en la lista
        actual.siguiente = None
        self.cola = actual
        self.numero_tareas -= 1

    def mostrar_tareas(self):
        actual = self.cabeza
        while actual:
            # Mostramos el nombre de la tarea y avanzamos al siguiente nodo
            print(actual.tarea)
            actual = actual.siguiente

    def mostrar_numero_tareas(self):
        # Mostramos la cantidad total de tareas en la lista
        print(f"EL Total de tareas que hay es : {self.numero_tareas}")

# Creamos un objeto de la clase HistorialTareas para manejar el historial de tareas
historial = HistorialTareas()

while True:
    # Mostramos las opciones al usuario y le pedimos que seleccione una
    print("Seleccione una opción =>")
    print("[1.] Agregar tarea ")
    print("[2.] Eliminar última tarea ")
    print("[3.] Mostrar tareas ")
    print("[4.] Mostrar número de tareas ")
    print("[0.] Salir ")
    opcion = int(input("Opción: "))
    try:
        opcion =int(opcion)
    except ValueError:
        print("ERROR, ingrese de nuevo :")
        continue

    if opcion == 1:
        tarea = input("Ingrese la  tarea que desee : > ")

        historial.agregar_tarea(tarea)
    elif opcion ==2:
        print("<<  Se va a eliminar una tarea >>")
        historial.eliminar_ultima_tarea() #elimina la ultima tarreea
    elif opcion ==3:
        print("..........Tareas en orden inverso al que se agregaron.... >")
        historial.mostrar_tareas()
    elif opcion == 4:
        # Mostramos la cantidad total de tareas en el historial
        historial.mostrar_numero_tareas()

    elif opcion == 0:
        # Salimos del programa
        break
    else:
        print("Opción incorrecta, Por favor seleccione otra.")
