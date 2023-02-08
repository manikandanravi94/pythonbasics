names = ['mani', 'gopal', 'dhanesh', 'anton', 'mykola']
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

names_copy = names.copy()

names_copy.append("sean")
names_copy.append("yevhenni")

print(names_copy)
names_copy.remove("sean")

print(names_copy)

names_copy2 = list(names)

print(names_copy2)

names_copy3 = list(["another", "way to", "implement", "list creation"])

print(names_copy3)

# Extend is used to iterate through the interables and append the items to the current list
names_copy2.extend(["another", "way to", "implement", "list creation"])

print(names_copy2)
#list.sort method is only useful for small case string.. it will not work case-sensitive string
names.sort()
print(names)

# to sort in the reversed order
names.sort(reverse=True)
print(names)

# To work on the case-sensitive string, we need to use a sorted method and define the key=str.lower or str.casefold to sort
case_sensitive_names = ['mani', 'Gopal', 'dhanesh', 'anton', 'mykola']

case_sensitive_names=sorted(case_sensitive_names, key=str.lower,reverse=True)
print("ordered case sensitive name list")
print(case_sensitive_names)