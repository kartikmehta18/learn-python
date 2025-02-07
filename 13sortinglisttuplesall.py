li =[9,1,8,2,7,3,6,4,5]
# it store in new variable
sli = sorted(li)
print('Sorted list:', sli)
#reverse
slir = sorted(li, reverse=True)
print('Sorted reverse list:', slir)


li.sort()   # li.sort(reverse=True)
print(li)

# tuple
tup =(9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup) # it does not have this tup.sort()
print('Sorted tuple:', s_tup)

#dictionary
di ={'name':'Corey', 'job':'programming', 'age':None, 'os':'Mac'}
s_di=sorted(di)
print('Sorted dictionary:', s_di)


# objects sorting 
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)
    
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees =[e1,e2,e3]

# def e_sort(emp):
    # return emp.name

# s_employees = sorted(employees, key=e_sort) by name

s_employees = sorted(employees, key=lambda e: e.age)
print(s_employees)