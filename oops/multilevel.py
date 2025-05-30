class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
    
class C(A,B):
    varC="welcome to class C"
    
c1=C()
print(c1.varA)