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
        return str(self.re)+"+"+str(self.im)+"i"
        
class Addition:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    
    
    def __str__(self):
        return str(self.re+self.im)
           
                
        
c1 = Complex(1, 2)
c2 = Addition(1, 2)
print(c1)
print(c2)

