from termcolor import cprint
import hashlib as hl


def welcome():
    cprint("Welcome", 'red')


# New Acc Text

# Get User
# Check User
#   Request New If In Use
# Hold User


def signUp():
    print("Create a New Account")
    user = input("Enter a Username: ")
    # TODO Filter Username
    # Testing Case
    passwd = input("Enter a Password: ")
    confirm_passwd = input("Confirm your Password: ")
    if passwd == confirm_passwd:
        encode = passwd.encode()
        hash0 = hl.md5(encode).hexdigest()
        with open("users.txt", "w") as f:
            f.write(user + '\n')
            f.write(hash0)
        f.close()
        print("Registration Successful")
    else:
        print("Passwords do not match try again")
        signUp()


signUp()
