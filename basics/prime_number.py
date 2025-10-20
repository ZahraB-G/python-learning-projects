# Check whether a number is prime or not.
count = 0
num = int(input('Enter a number: '))
for i in range(1,num):
    if num % i == 0:
        count += 1
if count <= 2:
    print(f'{num} is prime.')
else:
    print(f'{num} is not prime.')