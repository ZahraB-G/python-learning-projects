# Check whether a given number is even or odd.
given_value = int(input('Enter your numeric value'))
if given_value % 2 == 0:
    print(f'{given_value} is even number')
else:
    print(f'{given_value} is odd number')

# Check if a person is eligible to vote based on their age. 
# The voter must be 18 or older.
age = int(input('Enter your age?'))
if age >= 18:
    print('You are eligible to vote.')
else:
    print('You are too young to vote.')

# Age check for work challenge. A person must be older than 18 years and younger than 60 years old to be eligible to work.
age = int(input('Enter your age?'))
if age >= 18 and age < 60:
    print('You are eligible to work.')
else:
    print('You are not eligible to work.')

# Valid mark for a grade from an exam.
mark = float(input('Enter your grade: '))
if mark >= 0 and mark <= 100:
    print('Your grade is valid!')
else:
    print('Your grade is not valid. The correct grade must be in the range of [0,100]')

