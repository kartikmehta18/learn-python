class Student:
    def __init__(self,name):
        self.name=name

s1=Student("shradha")
print(s1.name)

# del for delete
# del s1.name
# print(s1.name)

# if we put __acc it will be private


class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_no=acc_pass #private
        
acc1=Account("123456","aabcde")
print(acc1.acc_no)
# print(acc1.acc_pass)


class Per:
    __name="anonymous"
    
    def __hello(self):
        print("hello dev's")
    
    def welcome(self):
        self.__hello()
        
p1=Per()
print(p1.welcome())

