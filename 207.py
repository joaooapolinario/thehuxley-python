n, m = map(int, input().split())
t = {}

for i in range(n):
    k = list(map(int, input().split()))
    sm = sum(k)
    t[i] = sm

menor = min(t, key=t.get)

print(menor + 1)