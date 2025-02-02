class vector:
    def __init__(self, values):
        self.values = list(values)

    def __str__(self):
        return ':'.join(map(str, self.values))

    def __add__(self, other):
        return vector(v1 + v2 for v1, v2 in zip(self.values, other))

    def __radd__(self, other):
        return self.__add__(other)

    def __matmul__(self, other):
        return sum(v1 * v2 for v1, v2 in zip(self.values, other))

    def __getitem__(self, index):
        return self.values[index]
