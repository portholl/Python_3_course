class Sire:
    def __init__(self):
        self.parent = self.__class__.__bases__[0].__name__

    @property
    def x(self):
        return self.parent
