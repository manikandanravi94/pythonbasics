dict = {
    1: "mani",
    2: "dhanesh",
    3: "GOpal",
    5: "anton",
    4: "mykola",
    6: "yev"
}

print(dict)
# pop will pop the element with the key ggiven as  a param
print(dict.pop(2))
# pop item will pop the element from the bottom
print(dict.popitem())

print(dict)
# this method will return the default value if that particular key is not present in the dict
dict.setdefault(8, "no item found")

print(dict.get(8))

for item in dict.items():
    print(item)

for key, value in dict.items():
    print("key : " + str(key) + " value : " + value)

print("printing keys alone")
for i in dict.keys():
    print("key : " + str(i))

print("printing values alone")
for i in dict.values():
    print("value : " + str(i))

# adding a value

dict[7] = "yevheni"
print("after adding a value into the dict : " + dict.__str__())
print(dict.get(6))

# To check the value is
if 6 in dict:
    print("key 6 exist")
else:
    print("key 6 not exist")

# To update a value in the dict
print("below are the ways to update a value in the dict")

for key in dict.keys():
    if key == 1:
        dict[key] = "Manikandan"

dict.update({3: "Gopalakrishnan"})

print(dict)

# dict problems
# problem 1: find a first non-repeating char
print("problem 1 starts")
s = 'masscodermass'
char_map = {}
for char in s:
    if char in char_map:
        char_map.update({char: char_map.get(char) + 1})
    else:
        char_map[char] = 1;

# for better understanding printing the else block
for char, count in char_map.items():
    if count == 1:
        print(char)
    else:
        print(char + " counts more than 1 count of the char in the given string : " + str(count))

# real solution is below
print(" below is the optimized solution")
for char, count in char_map.items():
    if count == 1:
        print(char)
        break
print("problem 1 ends")
# problem 2: find a first repeating character

repeating_char_string = 'testrepeatchars';
repeat_find_list = []
for char in repeating_char_string:
    if char in repeat_find_list:
        print("first repeating character in a string : " + char)
        break
    else:
        repeat_find_list.append(char)
