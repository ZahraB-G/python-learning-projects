#The game begins by allowing the user to define a range by entering 
# a lower and an upper bound (for example, from A to B). Once the range is set, 
# the system randomly selects an integer that falls within this user-defined interval.
# The user's task is then to guess the chosen number using as few attempts as possible.
# The game provides feedback after each guess, helping the user refine their next guess
# based on whether their previous attempt was too high or too low.
import random as rd
low_bound = int(input('Enter the lower bound '))
high_bound = int(input('Enter the higher bound '))
actual_number = rd.randint(low_bound,high_bound)
guess_number = int(input('Enter your guess '))
while actual_number != guess_number:
    if guess_number > actual_number:
        print('Too high')   
    elif guess_number < actual_number:
        print('Too Low')
    guess_number = int(input('Enter your guess '))
else:
    print(f'{guess_number} Is a correct. \nGood Game Try again Later!')