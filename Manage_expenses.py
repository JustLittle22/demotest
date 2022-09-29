
def add_item(list_item, item):
    list_item.append(item)

def find_index_item(list_item, item_name):
    result = -1
    length = len(list_item)
    for i in range(length):
        if list_item[i]['name'] == item_name:
            result = i
    return result

def remove_item(list_item, item_name):
    if find_index_item(list_item, item_name) > -1:
        del list_item[find_index_item(list_item, item_name)]
    else:
        print(item_name, "not in list")

print("What do you want to do?\n"\
        "1. Add \n"\
        "2. Remove")
option = int(input("Select option 1 or 2: "))
name_input = input("item name: ")
expenses = [{'name':'an uong', 'cost': 10, 'date': '14/2'}]
if option == 1:
    cost_input = int(input("Item cost: "))
    date_input = input("Input date: ")
    item = {'name': name_input, 'cost': cost_input, 'date': date_input}
    add_item(expenses, item)
    print("Your expenses ", expenses)
elif option == 2:
    remove_item(expenses, name_input)
    print("Your expenses", expenses)
else:
    print("Invalid valid")
