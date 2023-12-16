import json

restname = "Welcome to the A1 restaurant"

def name_requirements(name):
    return name.isalnum()

def userpass_requ(password):
    return all([
        len(password) >= 8,
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password)
    ])

def read_user_data():
    try:
        with open('/media/dammala/software/dammala_file/python_training/trainingfile/resturentapp/user_data.json', 'r') as json_file:
            user_data = json.load(json_file)
        return user_data
    except FileNotFoundError:
        return {}

def write_user_data(user_data):
    with open('/media/dammala/software/dammala_file/python_training/trainingfile/resturentapp/user_data.json', 'w') as json_file:
        json.dump(user_data, json_file)

def login_page(user_name, user_pass):
    user_data = read_user_data()
    if user_name in list(user_data.keys()) and user_pass in list(user_data.values()):
        print("Select the table")


def userlogin():

    def loginapp():
        user_data = read_user_data()
        urs_name = input("Enter the name = ")
        if urs_name in list(user_data.keys()):
            urs_password = input('enter the password = ')
            return login_page(urs_name, urs_password)
        else:
            print("User Not Existing Sigup to Login...!".upper())

    userstatus = input("Please enter 'signup' or 'login': ")
    if userstatus == "signup":
        name = input("Enter the username: ")
        password = input("Enter the user password: ")

        existing_user_data = read_user_data()

        # Check if the username already exists
        if name in existing_user_data:
            print("Username already exists. Signup failed.")
        elif name_requirements(name) and userpass_requ(password):
        
            # Add new user data to the existing user data
            existing_user_data[name] = password

            # Write the updated user data to the JSON file
            write_user_data(existing_user_data)
            print("Signup successful!")

            print(f"Login to Access The {restname}")
            loginapp()
        else:
            print("Invalid username or password. Signup failed.")
    elif userstatus == "login":
        loginapp()
    else:
        print("Login functionality not implemented yet.")


# Call the userlogin function
userlogin()


