import heapq

class MyHeapq:
    def __init__(self, initial=None, key=lambda x:x):
        self.key = key
        self.index = 0
        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self._data)
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), self.index, item))
        self.index += 1


    def pop(self):
        if len(self._data) == 0:
            return None
        val = heapq.heappop(self._data)
        return val[2]

    def size(self):
        return len(self._data)