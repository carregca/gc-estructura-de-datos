# Pasa todos los elementos de un stack a otro
def transferir(pila_origen, pila_destino):

    while len(pila_origen) > 0:

        elemento = pila_origen.pop()
        pila_destino.append(elemento)


# Vacía una pila usando recursividad
def vaciar_pila(pila):

    if len(pila) == 0:
        return

    print(pila.pop())

    vaciar_pila(pila)


# Invierte una lista usando una pila auxiliar
def invertir_lista(lista):

    pila = []

    for elemento in lista:
        pila.append(elemento)

    for i in range(len(lista)):
        lista[i] = pila.pop()

    return lista


# Pila usando listas
pila = []

pila.append(5)
pila.append(3)

valor_pila = pila.pop()

print(pila)
print(valor_pila)


# Cola usando listas
cola = []

cola.append(5)
cola.append(3)

valor_cola = cola.pop(0)

print(cola)
print(valor_cola)


# Transferencia entre pilas
pila_origen = [1, 2, 3, 4]
pila_destino = []

transferir(pila_origen, pila_destino)

print(pila_origen)
print(pila_destino)


# Vaciar pila recursivamente
pila_recursiva = [1, 2, 3, 4]

vaciar_pila(pila_recursiva)

print(pila_recursiva)


# Invertir lista
lista = [1, 2, 3, 4, 5]

lista_invertida = invertir_lista(lista)

print(lista_invertida)