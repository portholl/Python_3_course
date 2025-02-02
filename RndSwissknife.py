import random
from collections.abc import Sequence, Iterable
def rnd(a, b=None):
    match (a, b):
        case (int(), int()):
            return random.randint(a, b)

        case (int(), None):
            return random.randint(0, a)

        case (float(), (int() | float())):

            return random.uniform(a, b)
        case (str(), int()):
            if b <= len(a):
                start = random.randint(0, len(a) - b)
                return ''.join(a[start:start + b])

        case (str(), str()):
            return random.choice(a.split(b))

        case (str(), None):
            words = a.split()
            if not words:
                return ""
            return random.choice(words)
        
        case (Sequence() | Iterable(), int()):
            return random.choices(list(a), k=b)

        case (Sequence() | Iterable(), None):
            return random.choice(list(a))

exec(__import__("sys").stdin.read(), globals())