import random
import time
import os

options = [
    'r',
    'p',
    's'
]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Clear the screen --> lambda: os.system('cls')

print(f'{bcolors.FAIL}You lost. {bcolors.BOLD}GG!{bcolors.ENDC}')

cls = lambda: os.system('cls')

def play():
    cls()
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n\n")
    computer = random.choice(options)

# Losses
# Chose rock and won

    if user == 'r' and computer == 'p':
        print('\nRock, Paper, Scissors, Shoot!\n')
        print("Computer chose paper")
        print(f'{bcolors.FAIL}You lost. {bcolors.BOLD}GG!{bcolors.ENDC}')

        def function_again():
            again = input("Would you like to play again? y/n\n\n")

            if again == 'y':
                print("\nOK. Reloading...")
                time.sleep(1.5)
                play()
            elif again == 'n':
                print("\nOK. Bye")
                time.sleep(1.5)
                print('Leaving...')
                time.sleep(2.5)
                exit()
            else:
                print("Sorry, I didn't get that")
                function_again()

        function_again()

# Chose paper and lost

    if user == 'p' and computer == 's':
        print('\nRock, Paper, Scissors, Shoot!\n')
        print("Computer chose scissors")
        print(f'{bcolors.FAIL}You lost. {bcolors.BOLD}GG!{bcolors.ENDC}')

        def function_again():
            again = input("Would you like to play again? y/n\n\n")

            if again == 'y':
                print("\nOK. Reloading...")
                time.sleep(1.5)
                play()
            elif again == 'n':
                print("\nOK. Bye")
                time.sleep(1.5)
                print('Leaving...')
                time.sleep(2.5)
                exit()
            else:
                print("Sorry, I didn't get that")
                function_again()

        function_again()

# Chose scissors and lost

    if user == 's' and computer == 'r':
        print('\nRock, Paper, Scissors, Shoot!\n')
        print("Computer chose rock")
        print(f'{bcolors.FAIL}You lost. {bcolors.BOLD}GG!{bcolors.ENDC}')

        def function_again():
            again = input("Would you like to play again? y/n\n\n")

            if again == 'y':
                print("\nOK. Reloading...")
                time.sleep(1.5)
                play()
            elif again == 'n':
                print("\nOK. Bye")
                time.sleep(1.5)
                print('Leaving...')
                time.sleep(2.5)
                exit()
            else:
                print("Sorry, I didn't get that")
                function_again()

        function_again()

# Wins
# Chose rock and won

    if user == 'r' and computer == 's':
        print('\nRock, Paper, Scissors, Shoot!\n')
        print("Computer chose scissors")
        print(f'{bcolors.OKGREEN}You won! {bcolors.BOLD}GG!{bcolors.ENDC}')

        def function_again():
            again = input("Would you like to play again? y/n\n\n")

            if again == 'y':
                print("\nOK. Reloading...")
                time.sleep(1.5)
                play()
            elif again == 'n':
                print("\nOK. Bye")
                time.sleep(1.5)
                print('Leaving...')
                time.sleep(2.5)
                exit()
            else:
                print("Sorry, I didn't get that")
                function_again()

        function_again()

# Chose paper and won

    if user == 'p' and computer == 'r':
        print('\nRock, Paper, Scissors, Shoot!\n')
        print("Computer chose rock")
        print(f'{bcolors.OKGREEN}You won! {bcolors.BOLD}GG!{bcolors.ENDC}')

        def function_again():
            again = input("Would you like to play again? y/n\n\n")

            if again == 'y':
                print("\nOK. Reloading...")
                time.sleep(1.5)
                play()
            elif again == 'n':
                print("\nOK. Bye")
                time.sleep(1.5)
                print('Leaving...')
                time.sleep(2.5)
                exit()
            else:
                print("Sorry, I didn't get that")
                function_again()

        function_again()

# Chose scissors and won

    if user == 's' and computer == 'p':
        print('\nRock, Paper, Scissors, Shoot!\n')
        print("Computer chose paper")
        print(f'{bcolors.OKGREEN}You won! {bcolors.BOLD}GG!{bcolors.ENDC}')

        def function_again():
            again = input("Would you like to play again? y/n\n\n")

            if again == 'y':
                print("\nOK. Reloading...")
                time.sleep(1.5)
                play()
            elif again == 'n':
                print("\nOK. Bye")
                time.sleep(1.5)
                print('Leaving...')
                time.sleep(2.5)
                exit()
            else:
                print("Sorry, I didn't get that")
                function_again()

        function_again()

# Ties
# Chose rock and tied

    if user == 'r' and computer == 'r':
        print('\nRock, Paper, Scissors, Shoot!\n')
        print("Computer chose rock")
        print(f'{bcolors.OKCYAN}You tied. {bcolors.BOLD}GG!{bcolors.ENDC}')

        def function_again():
            again = input("Would you like to play again? y/n\n\n")

            if again == 'y':
                print("\nOK. Reloading...")
                time.sleep(1.5)
                play()
            elif again == 'n':
                print("\nOK. Bye")
                time.sleep(1.5)
                print('Leaving...')
                time.sleep(2.5)
                exit()
            else:
                print("Sorry, I didn't get that")
                function_again()

        function_again()

# Chose paper and tied

    if user == 'p' and computer == 'p':
        print('\nRock, Paper, Scissors, Shoot!\n')
        print("Computer chose paper")
        print(f'{bcolors.OKCYAN}You tied. {bcolors.BOLD}GG!{bcolors.ENDC}')

        def function_again():
            again = input("Would you like to play again? y/n\n\n")

            if again == 'y':
                print("\nOK. Reloading...")
                time.sleep(1.5)
                play()
            elif again == 'n':
                print("\nOK. Bye")
                time.sleep(1.5)
                print('Leaving...')
                time.sleep(2.5)
                exit()
            else:
                print("Sorry, I didn't get that")
                function_again()

        function_again()

# Chose scissors and tied

    if user == 's' and computer == 's':
        print('\nRock, Paper, Scissors, Shoot!\n')
        print("Computer chose scissors")
        print(f'{bcolors.OKCYAN}You tied. {bcolors.BOLD}GG!{bcolors.ENDC}')

        def function_again():
            again = input("Would you like to play again? y/n\n\n")

            if again == 'y':
                print("\nOK. Reloading...")
                time.sleep(1.5)
                play()
            elif again == 'n':
                print("\nOK. Bye")
                time.sleep(1.5)
                print('Leaving...')
                time.sleep(2.5)
                exit()
            else:
                print("Sorry, I didn't get that")
                function_again()

        function_again()


play()
