def registration():
    login = input("login: ")
    with open("file.txt", "r+") as f:


        lines = f.readlines()
        for line in lines:
            print(line.strip())
        if login in lines:
            print("sorry this name already exists")
        else:
            g = str(input("password"))
            h = str(input("name"))
            s = f"{login} {g} {h}"
            f.write(s)


    ###после проверки login, что его нет в файле



def login():
    logins = input("login: ")
    password = input("password: ")

    with open("file.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
        if logins in lines:
            if password in lines:
                print("Helov word")

        else:
            print("sorry this password already exists")




while True:
    ans = int(input("Choose 1 - login, 2 - registration, 3 - exit: "))
    if ans == 1:
        login()
    elif ans == 2:
        registration()
    elif ans == 0:
        break
    else:
        print("Try again!")