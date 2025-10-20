# Given a list of numbers, use a while loop to add each value and print the final sum after processing all items.
numbers = [2,5,9,6,4]
n = len(numbers)
i = 0
sum = 0
while i < n:
    sum += numbers[i]
    i += 1
print(f'Total sum is {sum}')