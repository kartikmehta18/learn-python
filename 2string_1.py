


print("jai jinendra");


a="Hello World"
print(a);
# length of a string
print(len(a))
# print index
print(a[0])
# range of index
print(a[0:5])
print(a[:5])
print(a[5:])


# lowercaseje  
print(a.lower())

# uppercase
print(a.upper())
# counting letter
print(a.count('l'))
# find the letter ay index
print(a.find('World'))

# replace word
new_a = a.replace('World','universe')
print(new_a)

# concate the two string
b= "hello"
c="kartik"

# message= b + " " + c + " " + "welcome"
# message= ' {}, {} welcome'.format(b,c)
message= f'{b}, {c.upper()} welcome'

print(message)


#dri
print(dir(c))

# print(help(str)) 