#Stacks y Queues
#¿Qué valores te devuelve la siguiente serie de operaciones, si las ejecutás sobre un stack inicialmente vacío?: push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(), pop(), push(4), pop(), pop().  
#Implementa una versión de Stack y una de Queue con listas de Python. Luego, implementá ambas estructuras usando programación orientada a objetos.
#Implementá una función transfer(S, T) que pase todos los elementos del stack S al stack T, de forma tal que el elemento que arranca en el tope de S sea el primero en insertarse en T, y el elemento que está en el fondo de S termine quedando en el tope de T.  
#Armá un método recursivo para sacar todos los elementos de un stack.
#Implementá una función que invierta una lista de elementos apilándolos en un stack en un orden, y volviéndolos a escribir en la lista en orden inverso.
#Suponé que una queue Q inicialmente vacía ejecutó un total de 32 operaciones enqueue, 10 operaciones peek y 15 operaciones dequeue, de las cuales 5 tiraron errores Empty (vacío) que fueron atrapados e ignorados. ¿Cuál es el tamaño actual de Q?

#Algunos ejercicios un poco más desafiantes (traten de pensar cómo pueden resolver cada problema aprovechando lo que saben de Stacks y Queues):
#Estamos trabajando con una cadena de texto (string) que consta de N caracteres. Estos caracteres únicamente contienen signos de agrupación del siguiente conjunto: {[()]}. Es decir, hay tres tipos de signos correctos: corchetes, paréntesis y llaves, y cada uno de los tres puede ser de apertura o de cierre. En total, son 6 caracteres posibles.
#Lo que debemos hacer es determinar si la cadena está correctamente “anidada”. Se considera que está correctamente anidada si se cumple alguna de las siguientes condiciones:
#Es una cadena vacía;
#Tiene el formato (X), [X] o {X}, donde X es una cadena correctamente anidada;
#Tienen el formato XY, donde X e Y son cadenas correctamente anidadas.
#	Se debe devolver 1 si la cadena está correctamente anidada y 0 si no lo está.
#Condiciones y restricciones: N se encuentra dentro del rango [0 … 200.000], por lo que también se contempla el caso de una cadena vacía. Además, podemos dar por sentado que la cadena siempre estará compuesta exclusivamente por los 6 caracteres mencionados anteriormente.
#Consideremos un río y N peces nadando en él. Algunos nadan río arriba y otros río abajo. Pueden comerse entre sí (y seguramente lo harán), si se les presenta la oportunidad. Podemos imaginar que un par de peces empezará a pelear (y uno se comerá al otro) si nadan en direcciones opuestas, no hay otros peces vivos entre ellos y eventualmente se encuentran.
#El pez más grande se comerá al más chico. Vamos a asumir que todos los peces nadan a la misma velocidad, lo que significa que los peces que se mueven en la misma dirección nunca llegarán a encontrarse. Nuestra tarea es determinar la cantidad de peces que logran mantenerse con vida.

#Nos dan dos arreglos (arrays), A y B. Ambos contienen la misma cantidad de elementos. A[i] representa el tamaño del pez número i, mientras que B[i] representa su dirección (0 para río arriba, 1 para río abajo). Debemos devolver la cantidad de peces que quedan vivos.
#Condiciones y restricciones: 
#N se encuentra dentro del rango [1 … 100.000], es decir, vamos a tener por lo menos un pez en ese río.
#Además, cada elemento del arreglo A es un número entero dentro del rango [0 … 1.000.000.000]
#Cada elemento del arreglo B solo puede tomar uno de los siguientes valores: 0 o 1.
#Por último, pero no menos importante, los elementos de A son todos distintos. Esto significa que si dos peces llegan a encontrarse y a pelear, nunca va a existir la posibilidad de que ambos tengan el mismo tamaño.

import random, os
from time import sleep

qeue= ["A", "B","C","A", "A", "C"]
stack= ["A", "B","C","A", "A", "C"]

menu= True
def borrador():
    sleep(1)
    os.system("cls" if os.name == 'nt' else "clear")

while menu:
    sq= input("que queres usar qeue o stack(q/s/x): ").lower()
    if sq== "q":
        subsubmenu= True
        while subsubmenu == True:

            borrador()
            hacer=input("que queres hacarle a la fila(e/d/p/v/t/s): ")

            if hacer == "e":
                borrador()
                #enqeue
                letra= random.randint(1,3)
                if letra== 1:
                    qeue.append("A")
                elif letra == 2:
                    qeue.append("B")
                else:
                    qeue.append("C")
                print("Qeue: ", qeue)
            elif hacer == "d":
                borrador()
                #deqeue
                element= qeue.pop(0)
                print("Ele.eli: ", element)
                print("Qeue: ", qeue)
            elif hacer == "p":
                borrador()
                #peek
                elemento= qeue[0]
                print(elemento)
            elif hacer == "v":
                borrador()
                #isempty
                if len(qeue) == 0:
                    print("true")
                else:
                    print("Falso")
            elif hacer == "t":
                borrador()
                #size
                print(len(qeue))
            elif hacer == "s":
                borrador()
                subsubmenu= False
            else:
                borrador()
                print("no esta dentro de las opciones")

    elif sq == "s":
            
            submenu = True

            while submenu:
                accion = input("que queres hacerle al stack(m/s/p/v/t/x): ").lower()

                if accion == "m":
                    borrador()
                    #push
                    letra = random.randint(1,3)
                    if letra == 1:
                        stack.append("A")
                    elif letra == 2:
                        stack.append("B")
                    else:
                        stack.append("C")
                    print("Stack: ", stack)
                elif accion == "s":
                    borrador()
                    #pop
                    elemento = stack.pop()
                    print("Ele.eli: ", elemento)
                    print("Stack: ", stack)
                elif accion == "p":
                    borrador()
                    #peek
                    elemento = stack[-1]
                    print(elemento)
                elif accion == "v":
                    borrador()
                    #isempty
                    if len(stack) == 0:
                        print("True")
                    else:
                        print("False")
                elif accion == "t":
                    borrador()
                    #size
                    print(len(stack))
                elif accion == "x":
                    borrador()
                    submenu = False
                else:
                    borrador()
                    print("no esta dentro de las opciones")
    elif sq == "x":
        menu= False

    else:
        borrador()
        print("elegi q o s")






