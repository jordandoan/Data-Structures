class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        val = self.storage.pop()
        self._sift_down(0)
        return val

    def get_max(self):
        if self.storage:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while self.hasParent(index) and self.storage[self.getParent(index)] < self.storage[index]:
            parent = self.getParent(index)
            self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
            index = parent

    def _sift_down(self, index):
        while self.hasLeftChild(index):
            left = self.getLeftChild(index)
            if self.storage[left] > self.storage[index]:
                larger_child = left
            if self.hasRightChild(index):
                right = self.getRightChild(index)
                if self.storage[right] > self.storage[left]:
                    larger_child = right
            if self.storage[index] >= self.storage[larger_child]:
                break
            self.storage[larger_child], self.storage[index] = self.storage[index], self.storage[larger_child]
            index = larger_child

    def hasParent(self, index):
        return (index-1) // 2 >= 0

    def hasLeftChild(self, index):
        return index*2+1 < self.get_size()

    def hasRightChild(self, index):
        return (index+1)*2 < self.get_size()

    def getLeftChild(self, index):
        return index*2+1

    def getRightChild(self, index):
        return (index+1)*2

    def getParent(self, index):
        return (index-1) // 2