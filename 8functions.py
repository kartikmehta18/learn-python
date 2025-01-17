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

student('math' ,"art", name='kartik' , age =21)