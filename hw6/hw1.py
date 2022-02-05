def mydecorator(funk):
    def inner(*args, **kwargs):
        print("що вмене в кармані")
        funk(*args, **kwargs)
    return inner

@mydecorator
def say(a,b,c):
    print(f"{a}, {b}, {c}")

say("телефон","наушніки","грощі")







def mydecorator(funk):
    def inner(*args, **kwargs):
        print("ви купили BRAWL PASS вам доступно тепер")
        funk(*args, **kwargs)
    return inner

@mydecorator
def say(a,b,c,d):
    print(f"{a}, {b}, {c}, {d}")

say("10 мегаящікав","15 балщих ящик","1000 монет","5 ящик")