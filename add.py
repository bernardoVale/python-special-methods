class Counter(object):

    def __init__(self):
        self._total = 0

    def __add__(self, other):
        if type(other) == int:
            self._total += other

    @property
    def total(self):
        return self._total


# Add method will be called using the binary operator '+'
d = Counter()
print(d.total)  # 0
d + 5
print(d.total)  # 5
