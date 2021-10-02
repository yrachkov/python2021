from collections import Counter
with open("file.txt", "r") as f:
    s = Counter(f.read())
    print(s)
    q, q2, q3 = None, None, None
    h, h2, h3 = 0, 0, 0
    for i,kes in s.items():
        if kes >= h:
            h3, q3, h2, q2, h, q = h2,q2,h, q, kes, i
        if kes >= h2:
            h2,q2,h,q= h,q, kes, i
        elif kes >=h3:
            h, q = kes,i

print(q,q2,q3)
