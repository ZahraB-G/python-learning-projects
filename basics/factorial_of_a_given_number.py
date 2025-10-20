# Calculate the factorial of a given number
num = int(input('Enter your number: '))
factorial = 1
for i in range(1, num+1):
    factorial *= i 
print(f'Factorial of {num} is {factorial}')
