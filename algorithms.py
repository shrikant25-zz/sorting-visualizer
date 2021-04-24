import math


class Sort:
    def __init__(self, list):
        self.list = list
        self.size = len(self.list)


class Bubble(Sort):
    def __init__(self, list):
        super().__init__(list)

    def bubble(self):
        for x in range(self.size - 1):
            for y in range(0, self.size - x - 1):
                if self.list[y].height > self.list[y + 1].height:
                    self.list[y].drawrect(3)
                    self.list[y + 1].drawrect(3)
                    self.list[y].height, self.list[y + 1].height = self.list[y + 1].height, self.list[y].height
                    self.list[y].drawrect(5, True)
                    self.list[y + 1].drawrect(5, True)
            self.list[self.size - x - 2].drawrect(2)
            self.list[self.size - x - 1].drawrect(8)
        self.list[0].drawrect(8)


class Insertion(Sort):
    def __init__(self, list):
        super().__init__(list)

    def insertion(self):
        i = 1
        while i < self.size:
            j = i
            while j > 0 and self.list[j - 1].height > self.list[j].height:
                self.list[j].drawrect(3)
                self.list[j - 1].drawrect(3)
                self.list[j - 1].height, self.list[j].height = self.list[j].height, self.list[j - 1].height
                self.list[j - 1].drawrect(8, True)
                self.list[j].drawrect(8, True)
                self.list[i].drawrect(2)
                j -= 1
            i += 1


class Heap(Sort):
    def __init__(self, list):
        super().__init__(list)

    def heap(self):
        self.heapify(self.size)
        end = self.size - 1
        while end > 0:
            self.list[end].drawrect(3)
            self.list[0].drawrect(3)
            self.list[end].height, self.list[0].height = self.list[0].height, self.list[end].height
            self.list[end].drawrect(8)
            self.list[0].drawrect(8)
            end -= 1
            self.siftDown(0, end)

    def heapify(self, count):
        start = math.floor((count - 1) / 2)
        while start >= 0:
            self.siftDown(start, count - 1)
            start -= 1

    def siftDown(self, start, end):
        root = start
        while (2 * root + 1) <= end:
            child = 2 * root + 1
            swap = root

            if self.list[swap].height < self.list[child].height:
                swap = child

            if child + 1 <= end and self.list[swap].height < self.list[child + 1].height:
                swap = child + 1

            if swap == root:
                return
            else:
                self.list[swap].drawrect(3)
                self.list[root].drawrect(3)
                self.list[root].height, self.list[swap].height = self.list[swap].height, self.list[root].height
                self.list[swap].drawrect(2)
                self.list[root].drawrect(5)
                root = swap


class Merge(Sort):
    def __init__(self, list):
        super().__init__(list)

    def merge(self):
        temp = [0 for _ in range(self.size)]
        width = 1
        while width < self.size:
            i = 0
            while i < self.size:
                self.bottomupmerge(i, min(i + width, self.size), min(i + 2 * width, self.size), temp)
                i = i + 2 * width
            self.copylist(temp)
            width *= 2

    def bottomupmerge(self, ileft, iright, iend, temp):
        i = ileft
        j = iright
        for k in range(ileft, iend):
            if i < iright and (j >= iend or self.list[i].height <= self.list[j].height):
                self.list[i].drawrect(5, True)
                temp[k] = self.list[i].height
                i += 1
            else:
                self.list[j].drawrect(1, True)
                temp[k] = self.list[j].height
                j += 1

    def copylist(self, temp):
        for i in range(self.size):
            self.list[i].drawrect(3)
            self.list[i].height = temp[i]
            self.list[i].drawrect(8)


class Quick(Sort):
    def __init__(self, list):
        super().__init__(list)

    def quick(self):
        self.quicksort(0, self.size - 1)

    def quicksort(self, low, high):
        if low < high:
            p = self.partition(low, high)
            self.quicksort(low, p)
            self.quicksort(p + 1, high)

    def partition(self, low, high):
        mid = int((high + low) / 2)
        pivot = self.list[mid].height
        self.list[mid].drawrect(2)
        i = low - 1
        j = high + 1
        while True:
            while True:
                i += 1
                if self.list[i].height >= pivot:
                    break
            while True:
                j -= 1
                if self.list[j].height <= pivot:
                    break
            if i >= j:
                self.list[mid].drawrect(8)
                return j
            self.list[i].drawrect(3)
            self.list[j].drawrect(3)
            self.list[i].height, self.list[j].height = self.list[j].height, self.list[i].height
            self.list[i].drawrect(8, True)
            self.list[j].drawrect(8, True)
            self.list[j].drawrect(8, True)
