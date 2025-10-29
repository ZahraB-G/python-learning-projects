# Print 4 items with their prices. Total length is 20.
# Hot Dog -----$30
# Donuts ------$40
# Burger ------$35
# Pizza -------$65
lst =[]
for i in range(4):
    item = input('Enter the item name ')
    price = input('Enter the price for this item ')
    dash = 20 - len(item) - len(price)
    dashes = '-'* dash
    lst.append(item+dashes+'$'+price)
for item in lst:
    print(item)
