# Dictionaries
# Creating a Dictionary

empty_dict = {}
print(empty_dict)

person = {
    'first_name' : 'Arshi',
    'last_name' : 'Khan',
    'age' : 20,
    'country' : 'Finland',
    'is_married' : False,
    'skills' : ['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {
        'street' : 'Space street',
        'zipcode' : '02210'
    }
}

# Dictionary Length
print(person)
print(len(person))

# Accessing Dictionary Items
print(person['first_name'])
print(person['last_name'])
print(person['skills'])
print(person['address']['street'])
print(person.get('city'))

# Adding Items to a Dictionary
person['job_title'] = 'Instructor'
person['City'] = 'Jaipur'
person['skills'].append('HTML')
print(person)

# Modifying Items in a Dictionary
person['first_name'] = 'Eyob'
person['age'] = 252
print(person)

# Checking Keys in a Dictionary
print('first_name' in person)

# Removing Key and Value Pairs from a Dictionary
person.pop('first_name')
print(person)
person.popitem()
print(person)
del person['is_married']

# Changing Dictionary to a List of Items
print(person.items())

# Clearing a Dictionary
# print(person.clear())

# Copy a Dictionary
per = person.copy()
print(per)

# Getting Dictionary Keys as a List
keys = person.keys()
print(keys)

# Getting Dictionary Values as a List

values = person.values()
print(values)

# 💻 Exercises: Day 8
dog = {}
print(dog)

dog = {'name' : 'Tiger',
       'breed' : 'BullDogs',
       'legs' : 'chondrodysplastic ', 
       'age' : 9
}
print(dog)

student = {'first_name' : 'Arshi',
           'last_name' : 'Khan', 
           'Gender' : 'Female', 
           'Age' : 20,
           'Marital_status' : 'Unmarried', 
           'skills' : ['Communication skills', 'Language Skills', 'Python', 'Ai/ML'],
           'country' : 'India', 
           'City' : 'Jaipur',
           'Address' : {
               'Street' : 'Gulabi Nager 2nd',
               'Pl.No' : 10,
               'District' : 'Bhankrota',
               'Landmark' : 'Madrse k samne wali gali'
           }
        }
print(len(student))

per = student['skills']
print(type(per))

pr = student.get('skills')
print(pr)
print(type(pr))
pr = student.keys()
print(pr)
pr = student.values()
print(pr)
pr = student['skills']
print(pr)

skill = ['React', 'Node']
student['skills'].extend(skill)
print(student)

li =student.keys()
print(li)
li = student.values()
print(li)

print(student.items())

print(student.pop('first_name'))
print(student)
print(student.popitem())
print(student)

del student['skills']

print(student)
