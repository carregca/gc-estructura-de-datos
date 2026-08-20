class Nodo:
    def __init__(self, prioridad, valor):
        self.priority = prioridad
        self.value = valor


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, prioridad, valor):
        nodo = Nodo(prioridad, valor)
        self.queue.append(nodo)

        i = len(self.queue) - 1

        while i > 0 and self.queue[i].priority < self.queue[i - 1].priority:
            self.queue[i], self.queue[i - 1] = self.queue[i - 1], self.queue[i]
            i -= 1

    def dequeue(self):
        if len(self.queue) == 0:
            return None

        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None

        return self.queue[0]

    def __str__(self):
        resultado = []

        for node in self.queue:
            resultado.append(
                f"Prioridad: {node.priority}, Valor: {node.value}"
            )

        return str(resultado)


def main():
    pq = PriorityQueue()

    pq.insert(3, "Juan")
    pq.insert(1, "Pedro")
    pq.insert(5, "Carlos")
    pq.insert(2, "Maria")

    print("Priority Queue:")
    print(pq)

    node = pq.peek()
    print("\nPeek:")
    print(node.priority, node.value)

    node = pq.dequeue()
    print("\nDequeue:")
    print(node.priority, node.value)

    print("\nPriority Queue:")
    print(pq)

    node = pq.dequeue()
    print("\nDequeue:")
    print(node.priority, node.value)


if __name__ == "__main__":
    main()
