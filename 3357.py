n = int(input())
p = int(input())
conv = 0

for i in range(n):
    p1 = int(input())
    p2 = int(input())
    if p1 + p2 >= p and (p1 and p2) != 0:
        conv += 1
print(conv)