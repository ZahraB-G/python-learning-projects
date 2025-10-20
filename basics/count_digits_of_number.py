# determine the number of digits in a given integer.
number = int(input('Enter your digits: '))
count = 0
while number > 0:
    count = count + 1
    number = number // 10
print(f'the total digit of your given number is {count} ')