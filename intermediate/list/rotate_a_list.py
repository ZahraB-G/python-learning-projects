# Rotate a list
list = [1,2,3,4,5,6]
rotated = []
n = int(input('By how many place rotate the list? '))
rotated = list[n:] + list[:n] 

print(f'The actual list is {list}\nThe rotated list is {rotated}')