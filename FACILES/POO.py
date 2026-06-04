import random
import os
from time import sleep


class Queue:

    def __init__(self):
        self.cola = ["A", "B", "C", "A", "A", "C"]

    def enqueue(self):

        letra = random.randint(1,3)

        if letra == 1:
            self.cola.append("A")
        elif letra == 2:
            self.cola.append("B")
        else:
            self.cola.append("C")

        print("Queue:", self.cola)

    def dequeue(self):

        if len(self.cola) > 0:

            elemento = self.cola.pop(0)

            print("Ele.eli:", elemento)
            print("Queue:", self.cola)

        else:
            print("La queue esta vacia")

    def peek(self):

        if len(self.cola) > 0:
            print(self.cola[0])
        else:
            print("La queue esta vacia")

    def isempty(self):

        if len(self.cola) == 0:
            print("True")
        else:
            print("False")

    def size(self):

        print(len(self.cola))


class Stack:

    def __init__(self):
        self.pila = ["A", "B", "C", "A", "A", "C"]

    def push(self):

        letra = random.randint(1,3)

        if letra == 1:
            self.pila.append("A")
        elif letra == 2:
            self.pila.append("B")
        else:
            self.pila.append("C")

        print("Stack:", self.pila)

    def pop(self):

        if len(self.pila) > 0:

            elemento = self.pila.pop()

            print("Ele.eli:", elemento)
            print("Stack:", self.pila)

        else:
            print("La stack esta vacia")

    def peek(self):

        if len(self.pila) > 0:
            print(self.pila[-1])
        else:
            print("La stack esta vacia")

    def isempty(self):

        if len(self.pila) == 0:
            print("True")
        else:
            print("False")

    def size(self):

        print(len(self.pila))


def borrador():

    sleep(1)
    os.system("cls" if os.name == 'nt' else "clear")


qeue = Queue()
stack = Stack()

menu = True

while menu:

    sq = input("que queres usar qeue o stack(q/s/x): ").lower()

    if sq == "q":

        subsubmenu = True

        while subsubmenu:

            borrador()

            hacer = input("que queres hacerle a la fila(e/d/p/v/t/s): ").lower()

            if hacer == "e":

                borrador()
                qeue.enqueue()

            elif hacer == "d":

                borrador()
                qeue.dequeue()

            elif hacer == "p":

                borrador()
                qeue.peek()

            elif hacer == "v":

                borrador()
                qeue.isempty()

            elif hacer == "t":

                borrador()
                qeue.size()

            elif hacer == "s":

                borrador()
                subsubmenu = False

            else:

                borrador()
                print("no esta dentro de las opciones")

    elif sq == "s":

        submenu = True

        while submenu:

            accion = input("que queres hacerle al stack(m/s/p/v/t/x): ").lower()

            if accion == "m":

                borrador()
                stack.push()

            elif accion == "s":

                borrador()
                stack.pop()

            elif accion == "p":

                borrador()
                stack.peek()

            elif accion == "v":

                borrador()
                stack.isempty()

            elif accion == "t":

                borrador()
                stack.size()

            elif accion == "x":

                borrador()
                submenu = False

            else:

                borrador()
                print("no esta dentro de las opciones")

    elif sq == "x":

        menu = False

    else:

        borrador()
        print("elegi q o s")