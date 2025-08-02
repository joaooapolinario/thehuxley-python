t1 = []
t2 = []
t3 = []
while True:
    try:
        n = input()
        t = int(input())
        if t == 1:
            t1.append(n)
        elif t == 2:
            t2.append(n)
        else:
            t3.append(n)
    except EOFError:
        break
print('Turma 1:')
for i in t1:
    print(i)
print('')
print('Turma 2:')
for i in t2:
    print(i)
print('')
print('Turma 3:')
for i in t3:
    print(i)
