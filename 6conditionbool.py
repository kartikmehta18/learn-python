# if True:  if false :  dosent exicute the print state ment
#     print("condition was true")

# if else elif

lang = 'python'
# a = input("enter")
  
if lang == 'python':
    print('conditional was True')
elif lang == 'java':
    print("it is a java")
elif lang == 'js':
    print("it is a js")
else:
    print("not match")
    
user ='Admin'
login = True  # " " , [] , {} Dictonaries, () , 0 empty this will give false answer

if user == 'Admin' and login:
# if user == 'Admin' or login: print admin page
    print('admin page')
else:
    print("bad creds")
    
a =[1,2,3] 

b =[1,2,3]
print(a==b) # true
print(a is b) # false
print(id(a) ) # id is different of both