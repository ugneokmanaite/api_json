import math

class Calc:

    def sqrt(self, num1):
        return math.sqrt(num1)

    def ceil(self, num1):
        return math.ceil(num1)

# # creating object
simple_calc = Calc()

print(simple_calc.sqrt(64))
print(simple_calc.ceil(14.6))