nums =[1,2,3,4,5,6,7,8,9,10]

# my_list =[]
# for n in nums:
#     my_list.append(n)
# print(my_list)
# or

my_list = [n for n in nums]
print (my_list)

#for square of numbers
my_list = [n*n for n in nums]
print (my_list)

#using map + lambda
my_list = map(lambda n: n*n, nums)
print (list(my_list))

#even numbers
my_list =[]
for n in nums:
    if n%2 ==0:
        my_list.append(n)
print(my_list)
