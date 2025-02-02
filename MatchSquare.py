import sys

class Descriptor:
    
    def __get__(self, instance, owner):
        print(self.__class__)
        return self.value

    def __set__(self, instance, value):
        self.value = value

class HeightDescriptor(Descriptor):
    def __set__(self, instance, value):
        self.value = value
        instance.w = value
    
    def __get__(self, instance, owner):
        return instance.w

class AreaDescriptor(Descriptor):
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        return instance.w * instance.w

class CenterDescriptor(Descriptor):
    def __set__(self, instance, value):
        if len(value) == 2:
            instance.x = value[0] - instance.w / 2
            instance.y = value[1] - instance.w / 2
        elif len(value) == 4:
            instance.x = value[0] + value[2] - instance.w / 2
            instance.y = value[1] + value[3] - instance.w / 2

    def __get__(self, instance, owner):
        return (instance.x + instance.w / 2, instance.y + instance.w / 2)

class Square:
    __match_args__ = 'x', 'y', 'w'
    s = AreaDescriptor()
    h = HeightDescriptor()
    center = CenterDescriptor()
    
    def __init__(self, x, y, w):
        self.x, self.y = x, y
        self.w = w
        self.center = [x + self.w / 2, y + self.w / 2]
        self.s = w * w
    

exec(sys.stdin.read())
