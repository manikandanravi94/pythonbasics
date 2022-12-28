secret_number = 7

guess_count = 0

guess_max_count = 3

print("""       Secret number hidden in this program,whoever finds it. 
              !they will get a chance to win a lottery!. 
                         number is between 0 - 10""")

while guess_count < guess_max_count:
    guessed_value = int(input(' Guess the number '))
    if guessed_value == secret_number:
        print('Correct guess!')
        break
    guess_count += 1
else:
    print('Guess count exceeded to find the secret number.. please try it next time')

