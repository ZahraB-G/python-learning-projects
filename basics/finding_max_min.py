# Given the list of numbers find the largest and smallest elements.
numbers = [12,45,7,89,23]
n = len(numbers)
i = 0
Max = float('-inf')
Min = float('inf')
while i < n:
    if Max < numbers[i]:
        Max = numbers[i]
    elif Min > numbers[i]:
        Min = numbers[i]
    i += 1
print(f'The max number is {Max} and the min number is {Min}')