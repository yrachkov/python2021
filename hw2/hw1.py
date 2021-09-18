a = {"12":1,"11":2,"22":12,"ddd":3}
s = {2:3}
a.update(s)
f = input("яке ми удалям")
a.pop(f)
q = input("праверка на наліча")
w = 0
r = 0
for i,vin in a.items():
    if i in q:
        w += 1
    if vin in g:
        r += 1


print("ключи")
print(w)
print("значеня")
print(r)

print(a)