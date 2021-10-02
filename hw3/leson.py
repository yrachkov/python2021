
def registration():
    login = input("login: ")
    with open("../hw4/file.txt", "a") as f:
        if login in f:
            f.read(login)
            g = input("password")
            f.read(g)
            h = input("name")
            f.read(h)
        else:
            print("sorry this name already exists")


    ###после проверки login, что его нет в файле



def login():
    logins = input("login: ")
    #password = input("password: ")
    with open("../hw4/file.txt", "r") as f:
        if logins in f:
            f.read(logins)
        else:
            print("sorry this name already exists")




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