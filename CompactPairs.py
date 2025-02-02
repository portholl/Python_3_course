from string import ascii_letters
from functools import wraps
class Pairs:
    __slots__ =  list(ascii_letters)
    
    def __init__(self, N):
        for i in range(52):
            value = (N + i - 1) % 52 + 1
            setattr(self, self.__slots__[i], value)
    
    @wraps(str)
    def __str__(self):
        sorted_attributes = sorted(self.__slots__, key=lambda name: getattr(self, name))
        return ' '.join(sorted_attributes)

