print('car game to understand the while loop')

command = ''

car_started = False

while command != 'quit':
    command = input('> ').lower()
    if command == 'start':
        if not car_started:
            car_started=True
            print('Car started')
        else:
            print('car already running')
    elif command == 'stop':
        if car_started:
            car_started = False
            print('Car stopped')
        else:
            print('car is not started yet')
    elif command == 'help':
        print("""
        'start' - to start the car
        'stop'  - to stop the car
        'quit'  - to exit from the game
        """)
    elif command == 'quit':
        print('Exiting from the game...')
        break
    else:
        print("Enter 'help' to know the commands this program works")
