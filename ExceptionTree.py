class ExceptionTree:
    def __init__(self):
        self.exceptions = {}

    def __call__(self, n):
        if n not in self.exceptions:
            class_name = f"Exception-{n}"
            count = n // 2
            while count > 0:
                if count in self.exceptions:
                    parent_class = self.exceptions[count]
                    break
                count //= 2
            else:
                parent_class = Exception

            new_exception = type(class_name, (parent_class,), {})
            new_exception.n = n  
            self.exceptions[n] = new_exception
        return self.exceptions[n]

