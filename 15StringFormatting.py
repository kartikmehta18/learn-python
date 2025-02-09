person = {'name':'jenn', 'age':23}

# sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
# print(sentence)

sentence = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
print(sentence)

# sentence = 'My name is {0[name]} and I am {1[age]} years old'.format(person)
# print(sentence)

l = {'name': 'John', 'age': 30}
sentence = 'My name is {name} and I am {age} years old'.format(**l)
print(sentence)


tag='h1'
text='this is a headline'

sentence='<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
sentence=f'<{tag}>{text}</{tag}>'

print(sentence)


# now object oriented way
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
pl = Person('Jack', 33)

sentence = 'My name is {0.name} and I am {0.age} years old'.format(pl)
print(sentence)
# for decimal places we want to use f at {;.2f}
sentence = '1 mb is equal to {:,} bytes'.format(1000**2)
print(sentence)

# date time
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)
# MORE COMPLEX
sentence= '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)