n = []
q = 0
for i in range(3):
    n.append(float(input()))
m = (n[0]+n[1]+n[2])/3
for j in n:
    if j > m:
        q += 1
print(q)