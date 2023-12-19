import json
import pandas as pd
from fuzzywuzzy import process

def lstitmemenu(func):
    def wrapper(*args, **kwargs):
        # print(f"the number of items in the menu are {func(*args, **kwargs)}")
        start = True
        usermenu = []
        while start:
            enter_aplpha = input('enter_alpha = ').lower()
            # print(func(data).items())
            if enter_aplpha in list(func(*args, **kwargs).keys()):
                # df = pd.DataFrame(func(*args, **kwargs)[enter_aplpha])
                df = pd.DataFrame([(list(d.keys())[0], list(d.values())[0]) for d in func(*args, **kwargs)[enter_aplpha]], columns=['Dish', 'Cooking Time'])
                # df = df.fillna('')
                print(df)
                # Print only the column headers
                column_headers = df.columns
                storemenu = input(f"Enter the item menu in {column_headers[0]} = ")
                keys_list = [list(item.keys())[0] for item in func(*args, **kwargs)[enter_aplpha]]
                if storemenu in keys_list:
                    usermenu.append(storemenu)
                else:
                    print("Item no exisitn in the list...")
                    countlen = len(keys_list)
                    print(countlen)
                    while countlen:
                        storemenu = input("Enter the item menu in list = ")
                        
                        if storemenu in keys_list:
                            usermenu.append(storemenu)
                            keys_list.clear()
                            break
                        else:
                            print("Incorrect name of item no existing")
                            # Find the closest match
                            closest_match, similarity_score = process.extractOne(storemenu, keys_list)

                            # Check if the similarity score is above a certain threshold (adjust as needed)
                            threshold = 80
                            if similarity_score >= threshold:
                                print(f"Are you Looking For: {closest_match}")
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

# addmenu("chatmasala", "15mits")
# addmenu(None, None)
def getmenulist():
    json_file_path = '/media/dammala/software/dammala_file/python_training/trainingfile/resturentapp/itemmenu.json'

    with open(json_file_path, 'r') as iteminfo:
        try:
            data = json.load(iteminfo)
            # pd_read = pd.read_json(data)
            # Convert the nested JSON data into a flat structure
            flat_data = [(letter, dish, time) for letter, dishes in data.items() for dish_info in dishes for dish, time in dish_info.items()]

            # Create a DataFrame
            df = pd.DataFrame(flat_data, columns=["Letter", "Dish", "Cooking Time"])

            return df
        except json.decoder.JSONDecodeError:
            # Handle the case when the file is empty or not valid JSON
            data = {}
            return data

# print(getmenulist())