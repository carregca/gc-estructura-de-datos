class Node:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value


class PriorityQueueHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, priority, value):
        node = Node(priority, value)

        self.heap.append(node)
        self.size += 1

        self.arrange(self.size)

    def arrange(self, k):
        while k // 2 > 0:

            if self.heap[k].priority < self.heap[k // 2].priority:
                self.heap[k], self.heap[k // 2] = \
                    self.heap[k // 2], self.heap[k]

            else:
                break

            k //= 2

    def minchild(self, k):

        if 2 * k > self.size:
            return None

        if 2 * k + 1 > self.size:
            return 2 * k

        if self.heap[2 * k].priority < self.heap[2 * k + 1].priority:
            return 2 * k

        return 2 * k + 1

    def sink(self, k):

        while 2 * k <= self.size:

            child = self.minchild(k)

            if self.heap[child].priority < self.heap[k].priority:

                self.heap[k], self.heap[child] = \
                    self.heap[child], self.heap[k]

                k = child

            else:
                break

    def dequeue(self):

        if self.size == 0:
            return None

        node = self.heap[1]

        self.heap[1] = self.heap[self.size]

        self.heap.pop()
        self.size -= 1

        if self.size > 0:
            self.sink(1)

        return node

    def peek(self):

        if self.size == 0:
            return None

        return self.heap[1]

    def __str__(self):

        resultado = []

        for i in range(1, self.size + 1):
            resultado.append(
                f"Prioridad: {self.heap[i].priority}, Valor: {self.heap[i].value}"
            )

        return str(resultado)


def main():
    pq = PriorityQueueHeap()

    pq.insert(3, "Juan")
    pq.insert(1, "Pedro")
    pq.insert(5, "Carlos")
    pq.insert(2, "Maria")

    print("Priority Queue Heap:")
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

    print("\nPriority Queue:")
    print(pq)


if __name__ == "__main__":
    main()