# single quote required at the print statment, whole line should be enclosed in the double quotes vice versa for double quotes
# """ .... """" --> print in the same format specified between triple double quotes

course = "Python's for beginners"

print(course)

course1 = 'Java for "advanced programmers"'

print(course1)

# to get the char at function we can use the following syntax
# first element refers from the start of the string second element refers the end of the sub string -ve value calculates from the reverse order

print(course[2:-1])
print(course[:])
print(course[0:])
print(course[:-3])
print(course[-3:])
print('Python' in course)

# String functions

print(course.upper())
print(course.title())

print(len(course1))

# below function returns the starting index of the string
print(course.find('Python'))

print(f'{course}')
