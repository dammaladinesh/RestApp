import json


def lstitmemenu(func):
    def wrapper(*args, **kwargs):
        print(f"the number of items in the menu are {func(*args, **kwargs)}")
        start = True
        usermenu = []
        while start:
            enter_aplpha = input('enter_alpha = ').lower()
            # print(func(data).items())
            if enter_aplpha in list(func(*args, **kwargs).keys()):
                print(func(*args, **kwargs)[enter_aplpha])
                storemenu = input("Enter the item menu in list = ")
                keys_list = [list(item.keys())[0] for item in func(*args, **kwargs)[enter_aplpha]]
                if storemenu in keys_list:
                    usermenu.append(storemenu)
                else:
                    print("Item no exisitn in the list...")
                    while len(keys_list):
                        storemenu = input("Enter the item menu in list = ")
                        print("Incorrect name of item no existing")
                        if storemenu in keys_list:
                            usermenu.append(storemenu)
                            keys_list.clear()
                    pass
            else:
                print("Item not found")
            responce = input("Do you wnat to add more item Y/N = ".lower())
            if responce in ['yes', 'y', 'Yes']:
                pass
            else:
                start = False
                print(usermenu)
    return wrapper

@lstitmemenu
def addmenu(itemname, time):
    json_file_path = '/media/dammala/software/dammala_file/python_training/trainingfile/resturentapp/itemmenu.json'

    try:
        with open(json_file_path, 'r') as iteminfo:
            try:
                data = json.load(iteminfo)
            except json.decoder.JSONDecodeError:
                # Handle the case when the file is empty or not valid JSON
                data = {}
    except FileNotFoundError:
        # Handle the case when the file doesn't exist
        data = {}

    first_letter = itemname[0].lower()

    # Check if the key already exists in the data
    if first_letter in data:
        # Check if the item is not already in the list
        item_exists = False
        for item_entry in data[first_letter]:
            if itemname in item_entry:
                item_exists = True
                break

        # If it's not in the list, append the item with the associated time
        if not item_exists:
            data[first_letter].append({itemname: time})
    else:
        # If the key doesn't exist, create a new list for the key with the item and time
        data[first_letter] = [{itemname: time}]

    with open(json_file_path, 'w') as iteminfo:
        json.dump(data, iteminfo, indent=2)

    return data

addmenu("chatmasala", "15mits")
