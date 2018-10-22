#Cameron Murphy
#10/1/18
#password program

def menu():
    choice = 0
    while choice==0:
        print("to sign up press 1")
        print ("to sign in press 2")
        choice = int(input("enter your choice"))
        if choice == 1:
            print("choice 1")
            username = get_username()
            password = get_password()
            choice = 0

            
        elif choice == 2:
            print("choice 2")
            login = check_account(username, password)
            return password, username, login
        else:
            print("that's not a valid option")
            menu()

def get_password():
    print("""Your password must start with a capital letter
and must contain atleast 1 symbol
and must be atleast 10 charecters long""")
    password = input("enter your password")
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("password is set")
        return password
    else:
        print("your password didnt mmeet the requirements")
        get_password()

def get_username():
        print("""only contain numbers and letters
can only contain 10 charecters and must contain at least 3 charecters""")
        username= input("enter your username")
        if username.isalnum() and len(username)<=10 and len(username)>=3:
             print("your username is set")
             return username
        else:
            print("your username didnt meet the requirements")
            get_username
                

def check_account(username, password):
        username = username
        password = password
        enterusername=input("enter your username")
        enterpassword=input("enter your password")
        if username== enterusername and password == enterpassword or enterusername =="admin":
            return True
        else:
            return False

def main():
    login = False
    password, username, login = menu()

    if login==True:
        print("you got in")
    else:
            print("access denied")
            menu()

main()
    
