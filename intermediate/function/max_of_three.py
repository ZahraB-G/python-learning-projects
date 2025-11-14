# Define a Python function using positional-only parameters
# that finds and returns the largest of three input numbers.
def max3(a,b,c,/):
    max_number = -1
    if max_number < a:
        max_number = a
    if max_number < b:
        max_number = b
    if max_number < c:
        max_number = c
    # max_number = max(a,b,c) using max() built-in function
    # if a>b and a>c: 
        #return a
    # elif b>c:
        #return b
    # else:
        #return c
    return max_number


print(f'the max number is {max3(10,23,45)}')