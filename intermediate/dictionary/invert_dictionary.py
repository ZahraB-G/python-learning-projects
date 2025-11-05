# Create another inverted dictionary which keys as the values and vice versa.
original_dictionary = {'a':1, 'b':2, 'c':1, 'd':2, 'e':3, 'f':2}
inverted_dictionary = {}
for key,value in original_dictionary.items():
    if value not in inverted_dictionary:
        inverted_dictionary[value] = {key}
    else:
        inverted_dictionary[value].add(key)
print(inverted_dictionary)