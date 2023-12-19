import json


def table_info():
    try:
        with open("/media/dammala/software/dammala_file/python_training/trainingfile/resturentapp/resttables.json", "r") as fileinfo:
            getinfo = json.load(fileinfo)

        # print(getinfo)

        #Uncomment the following lines if you want to enumerate and print key-value pairs
        for i, j in enumerate(getinfo.items()):
            print(f"{j[0]} Table with Each {j[1]} chairs")

        getuserchoise_table = input("Please Select the number of Table you want = ")
        getuserchoise_chair = input("Please Select the number of Chair you want = ")
        from restapp2 import getmenulist, addmenu
        print(getmenulist())
        print(addmenu("chatmasala", "15mits")
)


    except Exception as e:
        return f"An error occurred: {e}"

# # Call the function
# table_info()
