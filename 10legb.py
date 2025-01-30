#LEGE  lOCAL, ENCLOSING GLOBAL, BUILT-IN

# x = 'gloal x'  # global define

def test():
    global x # working as global variable
    x = 'local x'
    y='local y' # local define cannot acces out side of function
    print(y)
    print(x)
test()
print(x)

    