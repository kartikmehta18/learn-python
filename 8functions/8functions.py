def hellow_func():
    a =5+6
    print(a)
# hellow_func()

# value passing function

def greet_fun(greeting , name="name"):
    return '{}, /{}'.format(greeting , name)
# print(greet_fun("hi", "kartik"))    

# new asvance function we pass this in function *args, **kwargs it store default inp paramater 
#values or default any kind of data 

def student(*args, **kwargs):
    print(args) #touple
    print(kwargs) # dictonary key , vaalue


# student('math' ,"art", name='kartik' , age =21)

def student1(*args, **kwargs):
    print(args) #touple
    print(kwargs) # dictonary key , vaalue


courses =['math', 'art']
info = {'name': 'kartik', 'age': 21}

# student1(courses,info) this prints (['math', 'art'], {'name': 'kartik', 'age': 21}) we got all in touple we solve
student1(*courses,**info) # unpact the values 
 