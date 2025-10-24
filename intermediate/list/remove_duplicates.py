# From the original list create a new list which only has the unique values.
list1 = [3,5,7,9,3,6,5,2,3,7]
list2 = []
for item in list1:
    if item not in list2:
        list2.append(item)
print(list2)