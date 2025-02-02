class Sizer:
    
    def __get__(self, obj, cls):
        if hasattr(obj, '__len__'):
            return len(obj)
        elif hasattr(obj, '__abs__'):
            return abs(obj)
        return 0
    
def sizer(cls):
    cls.size = Sizer()
    return cls

