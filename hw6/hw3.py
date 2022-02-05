s = input(":")

def check(s):
    def mydecorator(funk):
        def inner(*args, **kwargs):
            if s == "admin":
                funk(*args, **kwargs)
                print(f"ви тепер можете вбивати когось")
            elif s == "user":
                funk(*args, **kwargs)
                print(f"грайте на здоровя у вашом розпаріженії вся карта")
            else:
                funk(*args, **kwargs)
                print(f"хто ви?")
        return inner
    return mydecorator

@check(s)
def say(s):
    print(s)

say(s)