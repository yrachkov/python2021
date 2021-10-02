def a(s,h):
    if s > 1:
        mid = s // 2
        m1 = a(s)
        m2 = a(h)
        return m1 if m1 < m2 else m2
    return s[0]

f = int(input(":"))
g = int(input(":"))
print(a(f,g))