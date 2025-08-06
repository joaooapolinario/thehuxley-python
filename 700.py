st = int(input())
h = st // 3600
resto = st % 3600
m = resto // 60
s = resto % 60

print(f'{h} h {m} m {s} s')