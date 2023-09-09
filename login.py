# This is Login Page
from userinfo import dict1
from userinfo import dict2

def email():
    global iemail
    iemail = input("\n" + "Enter your email: ")
    if iemail in dict1:
        password()
    else:
        print("No eMail found!")
        email()

def password():
    global ipassword
    ipassword = input("Enter your password: ")
    if ipassword == dict2[dict1[iemail]]:
        print('\n' + "Welcome ",dict1[iemail])
    else:
        print("eMail and Password dosen't match!", "\n")
        password()
