class Sort:
    def __init__(self, list):
        self.list = list
        self.size = len(self.list)

    def bubble(self):
        for x in range(self.size - 1):
            for y in range(0, self.size - x - 1):
                if self.list[y].height > self.list[y + 1].height:
                    self.list[y].drawrect(3)
                    self.list[y + 1].drawrect(3)
                    self.list[y].height, self.list[y + 1].height = self.list[y + 1].height, self.list[y].height
                    self.list[y].drawrect(8)
                    self.list[y + 1].drawrect(8)
            self.list[self.size - x - 2].drawrect(2)
            self.list[self.size - x - 1].drawrect(4)

    def insertion(self):
        i = 1
        while i < self.size:

            j = i
            while j > 0 and self.list[j - 1].height > self.list[j].height:
                self.list[j].drawrect(3)
                self.list[j - 1].drawrect(3)
                self.list[j - 1].height, self.list[j].height = self.list[j].height, self.list[j - 1].height
                self.list[j - 1].drawrect(4)
                self.list[j].drawrect(4)
                self.list[i].drawrect(2)
                j -= 1
            i += 1

    def heap(self):
        pass

    def merge(self):
        pass

    def quick(self):
        pass
