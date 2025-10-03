n = int(input())
nums = input().split(' ')

numeros = []
menor = 9999

for i in range(n):
    numeros.append(int(nums[i]))
    if int(nums[i]) < menor:
        menor = int(nums[i])
        
print(f'Menor valor: {menor}')
print(f'Posicao: {numeros.index(menor)}')