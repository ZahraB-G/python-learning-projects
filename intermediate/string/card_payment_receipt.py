# Take the credit card number as the input and display it like xxxx xxxx xxxx 5566
card_no = input('Enter Card No ')
print('xxxx '*3 +' ' + card_no[15:] )