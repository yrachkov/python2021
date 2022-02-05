def dec(n=1):
    def mydecorator(funk):
        def inner(*args, **kwargs):
            print("ви купили BRAWL PASS вам доступно тепер")
            for i in range(n):
                funk(*args, **kwargs)
        return inner
    return mydecorator

n = int(input(":"))

@dec(n)
def say(a,b,c,d):
    print(f"{a}, {b}, {c}, {d}")

say("10 мегаящікав","15 балщих ящик","1000 монет","5 ящик")