from fractions import Fraction

class Sausage:
    def __init__(self, mince="pork!", volume=1):
        self.mince = mince
        self.volume = Fraction(volume) 
        self.full_length = 14 

    def __str__(self):

        if self.volume == 0:
            return "/|\n||\n||\n||\n\\|"
        
        full_sausage = int(self.volume)
        remainder_sausage = self.volume - full_sausage

        mince_ssusage = (self.mince * (12 // len(self.mince))) + self.mince[:12 % len(self.mince)]
        sausage_body = []
        v, m, n = "", "", ""
        r = int(remainder_sausage * 12)
        r_sausage = mince_ssusage[:r] 

        if full_sausage: 
            v = ("/" + "-" * 12+ "\\") * full_sausage
            m = (f"|{mince_ssusage}|") * full_sausage
            n = ("\\" + "-" * 12 + "/") * full_sausage
        if remainder_sausage:
            v += ("/" + "-" * (r) + "|")
            m += f"|{r_sausage}|"
            n += "\\" + "-" * (r) + "|"

        sausage_body.append(v)
        for _ in range(3):
            sausage_body.append(m)
        sausage_body.append(n)

        return "\n".join(sausage_body)

    
    def __add__(self, other):
        if isinstance(other, Sausage):
            return Sausage(self.mince, self.volume + other.volume)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Sausage):
            return Sausage(self.mince, max(self.volume - other.volume, 0))
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, int) and other >= 0:
            return Sausage(self.mince, self.volume * other)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, int) and other > 0:
            return Sausage(self.mince, self.volume / other)
        return NotImplemented
    
    def __abs__(self):
        return self.volume
    
    def __bool__(self):
        return self.volume > 0
