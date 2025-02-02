from functools import wraps

class Fix:
    def __init__(self, n):
        if (1 <= n <= 16):
            self.n = n
    
    def round_value(self, value):
        if isinstance(value, float):
            return round(value, self.n)
        return value
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            rounded_args = [self.round_value(arg) for arg in args]
            rounded_kwargs = {k: self.round_value(i) for k, i in kwargs.items()}

            result = func(*rounded_args, **rounded_kwargs)
            return self.round_value(result)

        return wrapper
