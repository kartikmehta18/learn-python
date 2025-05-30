class Car:
    color="black"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")
#single level inheritance       
class Toyotacar(Car):
    def __init__(self,brand):
        self.name=brand
    
#multilevel inheritance
class Fortuner(Toyotacar):
    def __init__(self,type):
        self.brand=type   
        
car1=Fortuner("petrol")
print(car1.start())
   
    
    
    
    
    

car1=Toyotacar("old model")
car2=Toyotacar("new model")

print(car1.start())
print(car1.color)


