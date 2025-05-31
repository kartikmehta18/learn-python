class Complex:
    def init (self, real,img) :
        self.real =real
        self.img = img
        
    def showNumber(self):
        print(self.real, "i +",self.img, "j " )
    
    def add(self,num2):    
        newReal=self.real + num2.real
        newiMG=self.img + num2.img
        return Complex(newReal,newiMG)
    
num1= Complex(1,3)
num1.showNumber()
    
num2= Complex(4, )
num2.showNumber()
num3=num1.add(num2)
num3.showNumber()