import emoji


class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"remaining: {emoji.emojize(self._size * ':cookie:')}"

    def deposit(self, n):
        self.size = self.size + n
        return self.size

    def withdraw(self, n):
        self.size = self.size - n
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("Size cannot be higher than capacity")
        elif size < 0:
            raise ValueError("Size cannot be lower than 0")
        self._size = size


def main():
    capacity = 12
    size = 0
    d = 5
    w = 4

    jar = Jar(capacity, size)
    jar.deposit(d)
    jar.withdraw(w)
    print(jar)


if __name__ == "__main__":
    main()