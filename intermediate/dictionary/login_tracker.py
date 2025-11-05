# Generate a dictionary for the users and tracking how many times
users = ['John', 'Bob', 'Alex', 'Alice', 'Charlie', 'John', 'Alex', 'Alice', 'John', 'Alex','Yara']
result = {}
for item in users:
    result[item] = users.count(item)
print(result)
