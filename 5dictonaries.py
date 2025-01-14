

student = {'name': 'john' , 'age':25 ,"course": ['maths', "ds"]}
print(student['course'])
print(student.get("name"))

student['phone']='555-55555'
print(student.get("phone",'not found'))
print(student)
# updte
student.update({'name': 'john' , 'age':25 ,"course": ['maths', "ds"], 'phone':555-55555})

# delete
# del student['age']

# pop is to delete val
pp = student.pop("age")

print(student)
print(pp)
print(student.items()) # print item
print(student.keys()) # print key

# for method

for key in student:
    print(key)
    
# for method for both key and value
for key,value in student.items():
    print(key , value)