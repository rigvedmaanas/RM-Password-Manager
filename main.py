from Crypto.Cipher import AES
import hashlib, uuid
from prettytable import PrettyTable
import os
import time

password = "STRONG_PASSWORD1"
passwords = ""
current_id = 0

salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

def encrypt(text, password):
    obj = AES.new(password, AES.MODE_CFB, 'This is an IV456')
    ciphertext = obj.encrypt(text)
    return ciphertext
def decrypt(text, password):
    obj = AES.new(password, AES.MODE_CFB, 'This is an IV456')
    ciphertext = obj.decrypt(text)
    ciphertext = str(ciphertext)
    ciphertext = ciphertext[2::]
    ciphertext = ciphertext[:-1]
    return ciphertext

run = True
stop = False
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
f = open("menu.txt", "r")
menu = f.read()
f.close()
try:
    while run:
        f = open('logo.txt', "r")
        print(f.read())
        f.close()
        print("WELCOME TO RM PASSWORD MANAGER")
        print("HERE YOUR INFORMATION IS SAFE")

        time.sleep(3)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        major_pass = input("Enter the password to enter: ")
        print()
        major_pass = hashlib.sha512(major_pass.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        if major_pass == hashed_password:
            major_pass = ""
            print("Signed In Successful!!!")
            while stop == False:

                f = open("nothinghere.txt", "r")
                text = "passwords = " + f.read()
                exec(text)
                f.close()


                print(menu)

                asked = input("Type the corresponding numbers to run the function!!!: ")
                try:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")

                    if int(asked) == 1:
                        f = open("nothinghere.txt", "r")
                        text = "passwords = " + f.read()
                        exec(text)
                        f.close()
                        print()
                        table = PrettyTable()
                        table.field_names = ["Id", "Website", "User Name", "Password", "Email Id"]
                        my_list = []
                        count = 0
                        for x in passwords:
                            my_list.append(count)
                            count += 1
                            for y in x:
                                my_list.append(str(decrypt(x[y], password)))

                            table.add_row(my_list)
                            my_list = []
                        my_list = []
                        print(table)
                        print()
                    elif int(asked) == 2:
                        dict_cred = {}
                        website = input("Website: ")
                        website = encrypt(website, password)
                        email_id = input("Email Id: ")
                        email_id = encrypt(email_id, password)
                        username = input("User Name: ")
                        username = encrypt(username, password)
                        password2 = input("Password: ")
                        password2 = encrypt(password2, password)
                        password3 = input("Confirm Password: ")
                        password3 = encrypt(password3, password)
                        if password2 == password3:
                            sure = input("Are You Sure You Want Add This Credentials? (Y/N): ")
                            if sure.lower() == "y":

                                dict_cred["Website"] = website
                                dict_cred["User Name"] = username
                                dict_cred["Password"] = password2
                                dict_cred["Email"] = email_id
                                passwords.append(dict_cred)
                                dict_cred = {}
                                f = open("nothinghere.txt", "w")
                                f.write(str(passwords))
                                f.close()

                                print("Action Was Successful")
                            else:
                                print("Invalid Prompt or User Cancelled")
                    elif int(asked) == 3:
                        id_to_delete = input("Enter the 'Id' to delete a Credential: ")
                        try:
                            id_to_delete = int(id_to_delete)
                            passwords.pop(id_to_delete)
                            f = open("nothinghere.txt", "w")
                            f.write(str(passwords))
                            f.close()
                            print("Action Successful")
                        except:
                            print()
                            print("This Id was not found")
                            print("Action cancelled")
                            print()
                    elif int(asked) == 4:
                        print("Thank You...... See You Later.....")
                        print("Don't Forget To Remember The Password")
                        quit()

                    else:
                        print("Invalid Command")
                except:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")



        else:
            print("Access Denied")
            run = False
except:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
