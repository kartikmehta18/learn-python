from urllib.response import addinfo


def even_odd(num):
    if num%2==0:
        # print(num)
        print("the {} is event".format(num))
    else:
        print("the {} is odd".format(num))
    
even_odd(9)   
    

lst =[1,2,3,4,5,6,734,56,34]


list(map(even_odd,lst))

# lambda

addition =lambda a,b:a+b
print(addition(12,13)) 

def even(num):                             
    if num%2==0:
        return True


lst1 =[1,2,0,7,56,34]
print(list(filter(even,lst1)))

km=print(list(filter(lambda num:num%2==0,lst1)))
print(km)