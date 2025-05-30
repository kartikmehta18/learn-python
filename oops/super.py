class Car:
   
    def  __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")
#single level inheritance       
class Toyotacar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()
    
car1=Toyotacar("pirus","electric")
# print(car1.start())
print(car1.type)



