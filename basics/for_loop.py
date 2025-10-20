# Print only Odd numbers
# First Method
max_number = int(input('Give your number'))
if max_number % 2 == 0:
    for i in range(0,max_number,2):
        print(i)

else:
    for i in range(0,max_number-1,2):
        print(i)
print('---------------------')
# Second Method
for i in range(max_number):
    if i % 2 == 0:
        print(i)
