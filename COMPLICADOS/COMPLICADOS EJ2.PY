def peces_vivos(A, B):

    pila = []
    vivos = 0

    for i in range(len(A)):

        tamaño = A[i]
        direccion = B[i]

        if direccion == 1:

            pila.append(tamaño)

        else:

            vivo = True

            while len(pila) > 0:

                if pila[-1] > tamaño:

                    vivo = False
                    break

                else:

                    pila.pop()

            if vivo:

                vivos += 1

    return vivos + len(pila)

A= [5, 6, 7]
B= [1, 1, 0]

print(peces_vivos(A, B))