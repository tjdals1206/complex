"""
name1: 문성민
name2:addition,subtraction
name3:multiplication
"""
class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    
    def __str__(self):
        return str(self.re) + "+" + str(self.im) + "i"
        
c1 = Complex(1,2)
print(c1)
    
