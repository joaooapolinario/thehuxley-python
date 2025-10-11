matriz_a = []
matriz_b = []

N, M, O = map(int, input().split())

matriz_c = [[0 for _ in range(O)] for _ in range(N)]

for i in range(N):
    linhas = map(int, input().split())
    matriz_a.append(list(linhas))

for j in range(M):
    linhas = map(int, input().split())
    matriz_b.append(list(linhas))
    
for i in range(N):
    for j in range(O):
        for k in range(M):
            matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]

for linha in matriz_c:
    print(*linha)

    