class heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.arrange(self.size)

    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def minchild(self, k):
        if 2 * k > self.size:
            return None

        if 2 * k + 1 > self.size:
            return 2 * k

        if self.heap[2 * k] < self.heap[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k):
        while 2 * k <= self.size:
            child = self.minchild(k)

            if self.heap[child] < self.heap[k]:
                self.heap[k], self.heap[child] = self.heap[child], self.heap[k]
                k = child
            else:
                break

    def delete_at_root(self):
        if self.size == 0:
            return None

        root = self.heap[1]

        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1

        if self.size > 0:
            self.sink(1)

        return root

    def delete_at_location(self, location):
        if location < 1 or location > self.size:
            return None

        if location == 1:
            return self.delete_at_root()

        deleted = self.heap[location]

        self.heap[location] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1

        if location <= self.size:
            if self.heap[location] < self.heap[location // 2]:
                self.arrange(location)
            else:
                self.sink(location)

        return deleted

    def heap_sort(self):
        result = []

        while self.size > 0:
            result.append(self.delete_at_root())

        return result

    def __str__(self):
        return str(self.heap[1:])


def main():
    h = heap()

    h.insert(10)
    h.insert(5)
    h.insert(20)
    h.insert(3)
    h.insert(8)
    h.insert(15)
    h.insert(1)

    print(h)

    print(h.delete_at_root())
    print(h)

    print(h.delete_at_location(2))
    print(h)

    print(h.heap_sort())


if __name__ == "__main__":
    main()