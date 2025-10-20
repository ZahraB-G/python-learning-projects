# Reverse a given number using a while loop.
given_number = int(input('Enter a number:'))
reversed = 0
while given_number > 0:
   reversed = reversed * 10 + given_number % 10
   given_number = given_number // 10
print(reversed)