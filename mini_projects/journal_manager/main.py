def read_all_entry():
    with open('./mini_projects/journal_manager/journal.txt','r') as file:
        data = file.readlines()
    return data

def show_data(data):
    for item in data:
        print(item)
    print('========================')

def add_entry(data):
    with open('./mini_projects/journal_manager/journal.txt','a') as file:
        file.write(data)

def search_entries(data):
    info = read_all_entry()
    for item in info:
        if data in item:
            print(item)


      
while True:
    print('==== File Journal Menu ====')
    print('1. Add Entry\n2. Read All Entries\n3. Search Entries\n4. Exit\n===========')
    option = int(input('Choose option (1-4):'))
    if option == 1:
        data = input('Write your journal entry: ')
        add_entry('\n'+data)
    elif option == 2:
        data = read_all_entry()
        show_data(data)
    elif option == 3:
        data = input('Enter the keyword')
        search_entries(data)
    elif option == 4:
        print('Thank you for your time')
        break
    else:
        print('Invalid Option!!!!')
