# Write a class called ComplexNumber, which takes in two attributes, 
# real part, and complex part, both default to 0.
 
# In mathematics, complex numbers are comprised of a real part and a complex part. 
# The complex part is denoted by the letter 'i'.
# example of a complex number 5 - 2i.
# the number i is formally defined as the sqrt of -1.
 
# Complex numbers have the following properties:
# i * i = -1
# (a + bi) + (c + di) = (a + c) + (b + d)i
# (a + bi) - (c + di) = (a - c) + (b - d)i
# (a + bi) * (c + di) = (a*c - b*d) + (a*d + b*c)i
# Example usage:


class ComplexNumber:
    def __init__(self, real_part=0, complex_part=0):
        # finish the class
        self.real_part = real_part
        self.complex_part = complex_part
        
    def __str__(self):
        return f"{self.real_part}+{self.complex_part}i"
        
    def __add__(self, other):
    #    (a + c) + (b + d)i
        real_sum = self.real_part + other.real_part
        complex_sum = self.complex_part + other.complex_part
        return ComplexNumber(real_sum, complex_sum)
        
    def __sub__(self, other):
        #(a - c) + (b - d)i
        real_dif = self.real_part - other.real_part
        complex_dif = self.complex_part - other.complex_part
        return ComplexNumber(real_dif, complex_dif)

    def __mul__(self, other):
        #(a*c - b*d) + (a*d + b*c)i
        real_prod = self.real_part * other.real_part - self.complex_part * other.complex_part
        complex_prod = self.real_part * other.complex_part + self.complex_part * other.real_part
        return ComplexNumber(real_prod, complex_prod)

cmplx = ComplexNumber(20, 4)
cmplx2 = ComplexNumber(2, 3)
print(cmplx)
print(cmplx2)
print()
print(cmplx + cmplx2)
print(cmplx - cmplx2)
print(cmplx * cmplx2)