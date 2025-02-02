def mix(*args):
    class Object:
        pass

    mixed = Object()
    
    for i in args:
        for j in dir(i):
            if j.startswith('_') or callable(getattr(i, j)):
                continue
            setattr(mixed, j, getattr(i, j))

    def new_str(self):
        attrs = {name: getattr(self, name) for name in dir(self) 
                 if not name.startswith('_') and not callable(getattr(self, name))}
        sorted_attrs = sorted(attrs.items())
        return ', '.join(f"{name}={value}" for name, value in sorted_attrs)

    Object.__str__ = new_str
    return mixed

exec(__import__("sys").stdin.read(), globals())