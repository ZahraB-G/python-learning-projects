# Prepare separate list for odd and even numbers in the list
lst = [4,8,3,5,10,7,2,9,13,6]
even_lst = [item for item in lst if item%2==0]
odd_lst = [item for item in lst if item%2 !=0]
print(f'Original list is {lst}\nOdd List is {odd_lst}\nEven List is {even_lst}')