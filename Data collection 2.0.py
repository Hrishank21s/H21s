#this is just to grind
#data collection using def

#above file is for getting the weather information after login.
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
    pass

def USER_LOGIN():
    username = input("USER NAME: ")
    password1 = input("ENTER PASSWORD: ")
    password2 = input("RE-ENTER PASSWORD: ")
    if password1==password2:
        try:
            filename = "user_data.txt"
            with open(filename, 'r') as file:
                user_data = file.read()
                if username in user_data and password1 in user_data:
                    print("Login successful!")
                    quit()
                else:
                    print("Invalid username or password. Please try again.")
        except FileNotFoundError:
            print("User data file not found.")
            No_data = input("Please let us know if you want to login?(Y/N): ").lower()
            if No_data == "y":
                print("Please mention the details below")
                USER_INFORMATION()
            else:print('Thanks for your time, Have a good one!')
            quit()
    else:
        print("PASSWORD IS NOT MATCHING!")
        USER_LOGIN()
    pass


def WELCOME():
    welcome_user = input("Hey! welcome to my first project, are you new here? (Y/N)").lower()
    if welcome_user == "y":
        SIGNUP = input("Great welcome onboard! please select '1' for continue signup or '2' for quit here.")
        if SIGNUP== "1":
            print("Thanks for moving forward, please mention your details below for onboarding!")
            USER_INFORMATION()
        elif SIGNUP== "2":
            print("Be back soon!")
            quit()
    elif welcome_user == "n":
        print("Ohh! Existing user, please login below.")
        USER_LOGIN()
    else:print("Invalid Command")
    quit()

