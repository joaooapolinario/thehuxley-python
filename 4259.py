p = [3.0, 2.5, 2.5, 1.0, 3.0]
cf = 0.0
for i in range(len(p)):
    n = int(input())
    if n > 0:
        cf += n*p[i]
print(f'conta final: {cf}')