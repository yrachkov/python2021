def a(x , y):
    if y == 0:
        return x
    else:
        return a(y, x % y)

d = int(input(':'))
s = int(input(':'))
if s == 0:
    print(d)
else:
    print(a(d,s))