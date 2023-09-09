# Main Page

print("Welcome to our python website!")
print("\n" + "Please login or signup to continue!")
def waysToContinue():
    # This function will ask user about the way to continue further through the Shop
    global loginType
    loginType = input("Type weather you want to login or signup (in small case) to continue:- ")
    if loginType == "login":
        from login import email
        email()
    elif loginType == "signup":
        from signup import signupeMail
        signupeMail()
    else:
        print("Enter the right way to continue!" + "\n")
        waysToContinue()

waysToContinue()

def OS():
    OsInput = input("Which OS based device would you like to see: ")
    if OsInput == "android" or OsInput == "Android":
        print("Entering android options.🙏")
    elif OsInput == "ios" or OsInput == "iOS" or OsInput == "Ios":
        print("Entering iOS options.🙏")
    elif OsInput == "blackberry" or OsInput == "Blackberry":
        print("Blackberry kon chalata hai chutiye!!")
    else:
        OS()

OS()
# just added this comment because i am learning github     