names = ['mani', 'Gopal', 'dhanesh', 'anton', 'mykola']
print(names[2:4])
print(names[2:-1])
print(names[2:])
print(names[:])

numbers = [1, 2, 5, 6, 3, 9, 8]
max = numbers[0]
for item in numbers:
    if item > max:
        max = item
        
print(max)
