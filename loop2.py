total_cart_amount = 0
prices = [10, 20, 30]

for price in prices:
    total_cart_amount += price

print(f'total value of a cart : {total_cart_amount}')

# we have a range function for for loop range (0,10,2) 0 dentoes start value of the variable, 10 denotes the max value 2 denotes the increment logic

for i in range(0, 10, 2):
    print(i)

numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print('*' * item)

# print 'F' without using inbuilt python function

for item in numbers:
    i = 0
    while i < item:
        print("*", end="")
        i += 1
    else:
        print()
