nums =[1,2,3,4,5,6,7,8,9,10]

# my_list =[]
# for n in nums:
#     my_list.append(n)
# print(my_list)
# or

# my_list = [n for n in nums]
# print (my_list)

#for square of numbers
# my_list = [n*n for n in nums]
# print (my_list)

#using map + lambda
# my_list = map(lambda n: n*n, nums)
# print (list(my_list))

#even numbers
# my_list =[]
# for n in nums:
#     if n%2 ==0:
#         my_list.append(n)
# print(my_list)

# alpabet and numbers
# my_list =[]
# for letter in 'abcd':
#     for nums in range(4):
#         my_list.append((letter,nums))
# print(my_list)

my_list =[(letter,num) for letter in 'abcd' for num in range(4)]
print (my_list)
#or

my_list=[n for n in nums if n%2 ==0]
print(my_list)

# using filter + lambda

my_list = filter(lambda n: n%2 ==0, nums)
print(list(my_list))

#dictonary comprehension 

names= ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros =['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

print (list(zip(names,heros)))

# my_dict ={}
# for name, hero in zip(names,heros):
#     my_dict[name] = hero
# print(my_dict)

#another method
my_dict={name: hero for name , hero in zip (names,heros) if name != 'Peter'}
print(my_dict)




#set comprehension

nums =[1,1,2,1,3,4,3,4,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print (my_set)


# generator expression
# I want to yield 'n*n' for each 'n' in nums
nums =[1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
       yield n*n
       
my_gen = gen_func(nums)

for i in my_gen:
    print(i)

my_gen =(n*n for n in nums)

lism=[]
def lst_squa(lst):
    for i in lst:
        lism.append(i*i)
    return lism


print(lst_squa([1,2,3,45,6,7]))

#LIST COMP
lsst=[[1,2,3,45,6,7]]
k=[i*i for i in lsst[0]]  # Access the first (and only) inner list
print(k)