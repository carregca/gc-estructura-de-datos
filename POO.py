# Clase Pila
class Pila:

    # Constructor
    def __init__(self):
        self.elementos = []

    # Agrega elementos a la pila
    def apilar(self, elemento):
        self.elementos.append(elemento)

    # Elimina el último elemento
    def desapilar(self):

        if len(self.elementos) == 0:
            return "Pila vacía"

        return self.elementos.pop()

    # Muestra el elemento del tope
    def cima(self):

        if len(self.elementos) == 0:
            return "Pila vacía"

        return self.elementos[-1]

    # Verifica si está vacía
    def vacía(self):
        return len(self.elementos) == 0


# Clase Cola
class Cola:

    # Constructor
    def __init__(self):
        self.elementos = []

    # Agrega elementos a la cola
    def encolar(self, elemento):
        self.elementos.append(elemento)

    # Elimina el primer elemento
    def desencolar(self):

        if len(self.elementos) == 0:
            return "Cola vacía"

        return self.elementos.pop(0)

    # Muestra el primer elemento
    def frente(self):

        if len(self.elementos) == 0:
            return "Cola vacía"

        return self.elementos[0]

    # Verifica si está vacía
    def vacía(self):
        return len(self.elementos) == 0


# Uso de Pila
pila = Pila()

pila.apilar(5)
pila.apilar(3)

print(pila.desapilar())
print(pila.cima())
print(pila.vacía())


# Uso de Cola
cola = Cola()

cola.encolar(5)
cola.encolar(3)

print(cola.desencolar())
print(cola.frente())
print(cola.vacía())