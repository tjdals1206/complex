"""
문성민 : maintainer
김동한 : addition,subtraction
조민식 : multiplication
"""

class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    
    
    def __str__(self):
        return str(self.re) + "+" + str(self.im) + "i"
              
    def multiply(self, c1): # (a+bi)(c+di)=ac+adi+bci-bd = (ac-bd) + (ad+bc)i
        c = Complex()
        c.re = self.re * c1.re - self.im * c1.im
        c.im = self.re * c1.im + self.im * c1.re
        return c
       
    def subtract(self, c1):
        c = Complex()
        c.re = self.re - c1.re
        c.im = self.im - c1.im
        return c
 
    def add(self, c1):
        c = Complex()
        c.re = self.re + c1.re
        c.im = self.im + c1.im
        return c
        
    def __add__(self, c): ## self _ c
        return self.add(c)
        
    def __sub__(self, c): 
        return self.subtract(c)
        
c1 = Complex(1, 2)
print(c1)
c2 = Complex(2, 3)

print(c1+c2)
print(c2-c1)
print(c1.multiply(c2))

