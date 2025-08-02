n1 = int(input())
k = 0
for i in range(20):
    num = int(input())
    if num == -1:
        break
    if n1 == num:
        k +=1
print(f'{n1} aparece {k} vezes')