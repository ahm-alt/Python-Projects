class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or capacity % 2 not in [0, 1]:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n > (self.capacity - self.size):
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

