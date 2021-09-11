a = int(input("ведіть число"))
b = input("ведіть знак")
c = int(input("ведіть число"))

if b == '+':
    print(a + c)

elif b == '-':
    print(a - c)

elif b == '*':
    print(a * c)

elif b == '/':
    print(a / c)

elif b == '//':
    print(a // c)

elif b == '%':
    print(a % c)

else:
    print("увас неравелний знак")
