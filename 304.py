n = int(input())
print(n)
ced = [100, 50, 20, 10, 5, 2, 1]
for i in ced:
    k, n = divmod(n, i)
    print(f'{k} nota(s) de R$ {i},00')