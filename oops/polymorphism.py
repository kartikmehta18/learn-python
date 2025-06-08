class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(f"{self.real} + {self.img}i")
    
    # def add(self, num2):
    # add dunder function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
# Create instances with both real and imaginary parts
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 0)  # Fix: img part missing, set to 0
num2.showNumber()
# num3 = num1.add(num2)
num3=num1+num2 # by dunder function add
num3.showNumber()
num3=num1-num2 # by dunder function sub
num3.showNumber()
