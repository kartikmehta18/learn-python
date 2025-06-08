class Circle :  
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return (22/7)* self.radius  **2
        
    def peri(self):
        return 2*  (22/7)* self.radius
c1=Circle(21)
print(c1.area())
print(c1.peri())



print("----------TASK2-----------")


class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetail(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
        
e1=Employee("SDE2","jio","9000000")
e1.showDetail()


print("-------TASK3--------")


class Engineer(Employee):
    def __init__(self,age,name):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","7,500,000")
        
eng1=Engineer("kartik",21)
eng1.showDetail()


print("-------TASK4--------")

class Order:
    def __init__(self,price,item):
        self.item=item
        self.price=price
        
    def __gt__(self,ordr2):
        return self.price > ordr2.price
    
ordr1=Order("chips",20)
ordr2=Order("coke",40)

print(ordr1 > ordr2)