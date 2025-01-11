courses = ["History" , "maths" ,"Sceince" ,"physics"]
print (courses[-1]) # for last items
print (courses[0])
print (courses[0:3]) #print f4rom 0  to 3 index but print 3 value

# append

courses.append("Data Science")  # append value at the end of list

print(courses)
courses.insert( 0,"Data Science") # insert the valuse at the given inedex
print(courses)

#insert method

courses1 = ["History" , "maths" ,"Sceince" ,"physics"]
courses2 = ["Javascript" , "react" ,"node"] # below this values are stored at index 0
# courses1.insert(0, courses2)
print(courses1)
print(courses1[0])

#extend method for soving above problem in line 17- 18 append also give same error

courses1.extend(courses2)
print(courses1)

#remove value
courses3 = ["History" , "maths" ,"Sceince" ,"physics"]
# courses3.remove("History")
print(courses3)

# pop it renove the last value 
popr = courses3.pop()
print(courses3)
print(popr)


#  methodes sort  list
list = ["History" , "maths" ,"sceince" ,"physics"]
# reverse
list.reverse()
print(list)
#sorting by alphabetial order
nums = [1,4,6,7,23,7,2,4,23,5,34]
# nums.sort()
nums.sort(reverse=True) # print in reverse order
print(nums)
# another is sorted function also / but we want to store that in some varaible
nums1 = [1,4,6,7,23,7,2,4,23,5,34]

ns = sorted(nums1)
print(ns)

# min max sum

print(min(nums1))
print(max(nums1))
print(sum(nums1))

# getting value index
list1 = ["History" , "maths" ,"Science" ,"physics"]
print(list1.index("Science"))

# checing value ans in bool

print("Science" in list1)
# for in loop

for item in list1:
    print(item)
 
# for print index and  item boath // also pass start param
for index ,item in enumerate(list1 , start=1):
    print(index,item)
    
# join at each value
list12 = ','.join(list1)
print(list12)

# we cant append in ( tuple )seen muatible example

# tup1=("History" , "maths" ,"Science" ,"physics")
# tup2 =tup1

# tup1[0]= "art" # cant appent 
# print(tup1)
# print(tup2)

# sets

cs= {"History" , "maths" ,"Science" ,"physics"}  # {} => this print the random value in the tuple
print(cs)

# intersection, differrence,union methhod
cs1= {"History" , "maths" ,"Science" ,"physics"}  
art= {"History" , "maths" ,"art" ,"design"}  

print(cs1.intersection(art))
print(cs1.difference(art))
print(cs1.union(art))