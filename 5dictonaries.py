

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
    
# for method for both the key and value 
for key,value in student.items():
    print(key , value)
    
    
    
    
#nested dictionary

stud ={
    "name":"rahul kumar",
    "subject":{
        "ai":97,
        "ml":90,
        "ds": 95
    }
}

# add sq baracket because we have in nested form data

print(stud["subject"])
print(stud["subject"]["ai"],"marks")
#keys print 
print(stud.keys())
print(stud.values())
print(list(stud.items()))
print(len(list(stud.keys())))

# geting values from key

# print(stud["name"])
# print(stud.get("name"))
# # when i write wrong key values 1st one give me error and second give me null
# # print(stud["name1"]) -->/ ERROR 
# print(stud.get("name1"))

up_dict={"name":"mehta ji","age":21}

stud.update(up_dict)
print(stud)