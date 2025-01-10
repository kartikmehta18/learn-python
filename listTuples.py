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
