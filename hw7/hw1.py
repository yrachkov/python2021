class Decorator:
    def __init__(self,fank):
        self.fank = fank

    def __call__(self, *args, **kwargs):
        print("Hello do you know programming languages")
        self.fank(*args,**kwargs)

@Decorator
def fank(a,b):
    print(a,b)

fank("Python","C++")