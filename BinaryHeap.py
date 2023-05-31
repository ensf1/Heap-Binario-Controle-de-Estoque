import math


class BinaryHeap:
    def __init__(self):
        self.heap_list = []
        self.size = 0

    def insert(self, node):
        self.heap_list.append(node)
        self._order_up(self.size - 1)
        self.size += 1

    def _order_up(self, index):
        while index > 0 and self.heap_list[index].factor() < self.heap_list[(index - 1) // 2].factor():
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def _order_down(self, index):
        minor = index
        left = index * 2 + 1
        right = index * 2 + 2

        if left < self.size and self.heap_list[left].factor() < self.heap_list[minor].factor():
            minor = left

        if right < self.size and self.heap_list[right].factor() < self.heap_list[minor].factor():
            minor = right

        if minor != index:
            self.swap(index, minor)
            self._order_down(minor)

    def swap(self, pos_x, pos_y):
        aux_x = self.heap_list[pos_x]
        self.heap_list[pos_x] = self.heap_list[pos_y]
        self.heap_list[pos_y] = aux_x

    # def find_min(self):

    def delete_min(self):
        if self.is_empty():
            return None
        minor = self.heap_list[0]
        self.swap(0, self.size - 1)
        self.heap_list.pop()
        self._order_down(0)
        self.size -= 1
        return minor

    def delete(self, index):
        if self.is_empty():
            return None

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def build_heap(self, list_to_heap):
        self.heap_list = []
        self.size = 0
        for item in list_to_heap:
            self.insert(item)
