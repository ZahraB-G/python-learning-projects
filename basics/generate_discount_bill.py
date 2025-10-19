# Generate Discount Bill 
# Discound for total amount bill less than 1000 is 10%, 
# for more than 1000 up to 5000 is 15%, 
# for more than 5000 up to 10000 is 20% 
# and more than that is 25%.
bill_amount = float(input('Enter your bill amount: '))
discount = 0
if bill_amount < 1000:
    discount = bill_amount * 0.1
elif bill_amount >= 1000 and bill_amount < 5000:
    discount = bill_amount * .15
elif bill_amount >= 5000 and bill_amount < 10000:
    discount = bill_amount * 0.2
else:
    discount = bill_amount * 0.25
total_amount = bill_amount - discount
print(f'total amount is {total_amount} \nwhich is the bill amount: {bill_amount} - discount amount : {discount}')