#This is the verson 2 of my data collection project with login and signup save file in .txt form
def USER_INFORMATION():
    full_name = input("What is your full Name?: ").lower()
    adhar_number = input("What is your Adhar number: ").lower()
    address = input("What is your permanent address: ").lower()
    phone_number = input("What is your contact number: ").lower()
    email = input("What is your primary email: ").lower()
    username = input("Create a unique user name: ")
    password = input("Please create a password: ")
    user_data = (f"Full_Name: {full_name}\nadhar_number: {adhar_number}\nEmail: {email}\nphone_number: {email}\nUsername:{username}\npassword:{password}\nADDRESS:{address} ")
    filename = "user_data.txt"
    print("Please verify your details below")
    print("NAME: ",full_name)
    print("ADHAR NUMBER: ",adhar_number)
    print("PHONE NUMBER: ", phone_number)
    print("ADDRESS: ",address)
    print("EMAIL: ",email)
    print("USER NAME: ",username)
    VERIFY = input("Is given data is correct? (Y/N)").lower()
    if VERIFY == "y":
        print("Thanks for the details!")
        with open(filename, 'w') as file:  # Using the correct filename variable
            file.write(user_data)
    elif VERIFY == "n":
        print("Ohh! snap, please re enter the details below")
        USER_INFORMATION()
    else:
        print("INVALID COMMAND!!!!")


def USER_LOGIN():
    username = input("USER NAME: ")
    password1 = input("PASSWORD: ")
    password2 = input("PASSWORD: ")
    if password1==password2:
        try:
            filename = "user_data.txt"
            with open(filename, 'r') as file:
                user_data = file.read()
                if username in user_data and password1 in user_data:
                    print("Login successful!")
                else:
                    print("Invalid username or password. Please try again.")
        except FileNotFoundError:
            print("User data file not found.")
            No_data = input("Please let us know if you want to login?(Y/N): ").lower()
            if no_data == "y":
                print("Please mention the details below")
                USER_INFORMATION()
            else:print('Thanks for your time, Have a good one!')
            quit()
    else:
        print("PASSWORD IS NOT MATCHING!")
        USER_LOGIN()




USER_LOGIN()
