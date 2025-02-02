class morse:
    def __init__(self, args=''):
        self.flag = True
        self.result = ''
        l = args.split(" ") if ' ' in args else list(args)

        self.dot, self.end_dot, self.dash = self._set_morse_values(l)
        self.result, self.sep_world, self.sep_symbols = self._set_separators(args, l)
        if len(l) == 4:
            self.result = l[3]
 
    def _set_morse_values(self, l):
        if len(l) == 0:
            return 'di', 'dit', 'dah'
        elif len(l) == 2:
            return l[0], l[0], l[1]
        return l[0], l[1], l[2]

    def _set_separators(self, args, l):
        if ' ' in args or (all(c.isalpha() for c in (self.dot, self.end_dot, self.dash)) and not args):            
            return '.', ', ', ' '
        return '', ' ', ''

    def __pos__(self):
        self.result = (self.end_dot if self.flag else self.dot + self.sep_symbols) + self.result
        self.flag = False
        return self

    def __neg__(self):
        self.result = (self.dash if self.flag else self.dash + self.sep_symbols) + self.result
        self.flag = False
        return self

    def __invert__(self):
        self.result = self.sep_world + self.result
        self.flag = True
        return self

    def __str__(self):
        return self.result