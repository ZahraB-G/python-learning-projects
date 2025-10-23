file = open('./intermediate/file_handling/data.txt','r')
data = file.read()
print(data)
file.close()
print('######################')
# With the below method there is no need to close the file. It closes automatically.
with open('./intermediate/file_handling/data.txt','r') as file:
    data = file.read()
print(data)