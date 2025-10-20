# Compute the sum of the digits of a given number
given_number = int(input('Enter your number: '))
sum = 0
while given_number > 0:
    sum = sum + (given_number %10)
    given_number = given_number // 10
print(sum)