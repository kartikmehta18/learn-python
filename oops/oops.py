class Student:
    # name="kartik"
    # default constreuctor
    def __init__(self):
        pass
    
    # paramaterize constructio
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        print("adding new student")
    

s1= Student("kartik",9)
print(s1.name,s1.cgpa)

s2= Student("shubh",10)
print(s2.name,s2.cgpa)






class Car:
    color="blue"
    brand="audi"
    
car1 = Car()
print(car1.color)
print(car1.brand)