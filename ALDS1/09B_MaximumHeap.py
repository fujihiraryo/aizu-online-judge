class Heap:
    def __init__(self, a) -> None:
        self.data = []
        for x in a:
            self.data.append(x)
        self.max = None
        for i in range(len(self.data) // 2)[::-1]:
            self.__heapify(self.data, i)

    def __heapify(self, a, i):
        n = len(a)
        if i * 2 + 1 < n and a[i * 2 + 1] > a[i]:
            self.max = i * 2 + 1
        else:
            self.max = i
        if i * 2 + 2 < n and a[i * 2 + 2] > a[self.max]:
            self.max = i * 2 + 2
        if self.max != i:
            a[i], a[self.max] = a[self.max], a[i]
            self.__heapify(a, self.max)


n = int(input())
(*a,) = map(int, input().split())
heap = Heap(a)
print(" ", end="")
print(*heap.data)
