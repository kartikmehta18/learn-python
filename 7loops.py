nums=[1, 2, 3, 4, 5]
for num in nums:
    print(num)

# break statment
for num in nums:
    if num== 3:
        print("found")
        break
    print(num)
    
 # continue statment it print found and then continue running
for num in nums:
    if num== 3:
        print("found")
        continue
    print(num)  
    
    #inner loop
for num in nums:
    for letter in "abc":
        print(num , letter)
        
# range fun range(10)
print("range fun")
for i in range(1 ,11): # it iterate till 10
    print(i)
    
# while loops
print("while")
x=0
while x<10:
    print(x)
    x+=1
    
    
x=0    
while True:
    if x==5:
        break
    print(x)
    x+=1
    
    
tup=(1,23,4,5,6,7,78,89,2,34,55,56)
idx=0
k= 2
for i in tup:
    idx+=1
    if i==k:
        print("got number x at index" ,idx)