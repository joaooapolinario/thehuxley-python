d = int(input())
km = int(input())

p = (30*d) + (0.01*km)
pf = p-(10/100*p)
print(f'{pf:.2f}')