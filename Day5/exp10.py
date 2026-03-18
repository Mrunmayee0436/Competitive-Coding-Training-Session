def login():
    username = input("Enter username : ")
    password = input("Enter password : ")

    if username == "mrunmayee" and password == "1234":
        print("Login successfully")
    else:
        print("Invalid credentials")

login()
