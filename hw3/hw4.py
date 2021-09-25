def a(lst):
    l = len(lst)
    if l > 1:
        mid = l // 2
        m1 = a(lst[:mid])
        m2 = a(lst[mid:])
        return m1 if m1 < m2 else m2
    return lst[0]
print(a())