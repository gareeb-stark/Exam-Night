# This is SignUp Page
import random
from userinfo import dict1
from userinfo import dict2

def signupeMail():
    # This funtion will work if the user selects E-Mail for continuing through the shop
    global eMail
    eMail = input("\n" + "Enter the E-Mail (currently we only suppport @gmail.com): ")
    if eMail in dict1:
        print("This eMail is already registered!")
        signupeMail()
    else:
        if len(eMail) > 10 and eMail[-10:] == "@gmail.com":
            uName()
        else:
            print("Enter the correct E-Mail")
            signupeMail()

def uName():
    global uname
    uname = input("\n" + "Enter the Username you want to use: ")
    if uname in dict2:
        print("Sorry the username is already taken!")
        uName()
    else:
        Password()

def Password():
    global password
    password = input("\n" + "Enter the password (must be atleast 8 characters): ")
    if len(password) < 7:
        print("Please follow the instructions")
        Password()
    else:
        captcha()

def captcha():
    ri = random.randint(10, 1000)  # This is the captcha
    ui = input("Enter the number " + str(ri) + " here: " )
    if ui == str(ri):
        print("\n" + "You are registered as " + uname + "\n")
        file = open('userinfo.py', 'a')
        storeIt = f"\ndict1[\"{eMail}\"] = \"{uname}\""
        storeIt2 = f"\ndict2[\"{uname}\"] = \"{password}\""
        file.write(storeIt)
        file.write(storeIt2)
    else:
        print("Wrong Captcha repeat the process again!" + "\n")
        captcha()