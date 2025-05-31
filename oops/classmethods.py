class Person:
    name ="anonymous"
    
    # def changeName(self,name):
    #     self.name=name
    #     # Person.name=name # this is method update class atribute 
    #     self.__class__.name = "kartik"  #another method 
        
    @classmethod
    def changeName(cls,name):
        cls.name=name 
           
        
p1 =Person()
p1.changeName("kartik") # NOW THIS WILL NOT UPDATE CLASS atribute 
print(p1.name)
print(Person.name)
    