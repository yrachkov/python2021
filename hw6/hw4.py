def mydecorator(funk):
    def inner(*args, **kwargs):
        print("ви купили BRAWL PASS вам доступно тепер")
        funk(*args, **kwargs)
        print("бонус")
    return inner

@mydecorator
def say(a,b,c,d):
    print(f"{a}, {b}, {c}, {d}")

def p(v):
    print(f"{v}")

say("10 мегаящікав","15 балщих ящик","1000 монет","5 ящик")
p("1000 старпоінтав")