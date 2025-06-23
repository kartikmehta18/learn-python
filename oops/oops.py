class Student:
    # name="kartik"
    # default constructor
    
    college_name= "piet"
    
    def __init__(self):
        pass
    
    # paramaterize constructio
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        print("adding new student")
        
    def welcome(self):
        print("welcome student",self.name)
    
    def get_marks(self):
        return self.cgpa
    
# s1= Student("kartik",9)
# print(s1.name,s1.cgpa)

s2= Student("shubh",10)
print(s2.name,s2.cgpa)
s2.welcome()
print(s2.get_marks())


# class Car:
#     color="blue"
#     brand="audi"
    
# car1 = Car()
# print(car1.color)
# print(car1.brand)



print("----------TASK--------")


class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def avg(sellf,marks):
        sum=0
        for i in marks:
            sum=sum+i
        av=sum/3
        print("your avg scoer is",av)
            
        
s1= Students("kartik",[99,89,80])
print(s1.name,s1.marks)
s1.avg([99,89,80])