# type conversion
# str() --> convert to string
# int() --> convert to integer
# bool() --> convert to boolean
# to check the type of variable, we can use type()

birth_year = input('what is your birth year ? ')

age = 2022 - int(birth_year)

print("your age as of 2022 is " + str(age))

print(type(age))

# Exercise convert pound to weight

weight_in_pounds = input("Please provide your weight in pounds : ")
weight_in_kgs = float(weight_in_pounds) / 2.2046
print(
    "your weight given in pounds " + str(weight_in_pounds) + " been calculated in kgs and your weight in kgs : " + str(
        weight_in_kgs))
