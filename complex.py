"""
문성민: maintainer
김동한: addition,subtraction
조민식: multiplication
"""
class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    
    def __str__(self):
        return str(self.re) + "+" + str(self.im) + "i"
        
        
    def subtract(self, c1):
        c = Complex()
        c.re = self.re - c1.re
        c.im = self.im - c1.im
        return c
        
c1 = Complex(1,2)
print(c1)
c2 = Complex(2, 3)
print(c1.subtract(c2))
