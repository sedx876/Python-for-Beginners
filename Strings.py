course = "Python for Beginners"
print(course)

what_course = 'Python for "Beginners"'
print(what_course)

email = '''
Hi John,

Here is our first email to you!!!

Thank you,
The Support Team

'''
print(email)
#index from a string
print(course[5])
print(course[0:3])

first = 'Sharon'
last = 'Watkins'

message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)
print(len(course))
print(course.upper())
print(course.find('P'))
print(course.replace('Beginners', 'Absolute Beginners').upper())
print('Python' in course)
