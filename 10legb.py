#LEGE  lOCAL, ENCLOSING GLOBAL, BUILT-IN

# x = 'gloal x'  # global define

# def test():
#     global x # working as global variable
#     x = 'local x'
#     y='local y' # local define cannot acces out side of function
#     print(y)
#     print(x)
# test()
# print(x)


def test(z):
    y='local y' # local define cannot acces out side of function
    print(y)
    print(z)
test("local z")

# bultin function in python


import builtins
# print(dir(builtins))

def my_min():
    pass

# m= min([5,1,4,2,3])
# print(m)

#enclosing have nested function

def outer():
    x='outer x' # when we comment this got error             
    def inner():
        nonlocal x #  nonlocal working as global variable
        x='inner x' # when we comment this got outer X ans
        print(x)
    inner()
    print(x)
outer()
    