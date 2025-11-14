# Write a addition function with variable length arguments
def add(*args):
    #return sum(args) using built-in function 
    sum = 0
    for item in args:
        sum += item
    return sum

print(f'Addition of 1 + 2 + 3  is {add(1,2,3)}')
print(f'Addition of 1 + 2 + 3 + 4 is {add(1,2,3,4)}')
print(f'Addition of 1 + 2 + 3 + 4 + 5 is {add(1,2,3,4, 5)}')