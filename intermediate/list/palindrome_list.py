# Find whether a list is palindrome or not
list = input('Enter your list? ')
reversed_list = list[::-1]
if list == reversed_list:
    print(f'{list} is Palindrome.')
else:
    print(f'{list} is NOT Palindrome.')