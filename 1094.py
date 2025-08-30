c1_total = 0
c2_total = 0
c3_total = 0
vb_total = 0
vn_total = 0

eleicao = {}
while True:
    sec = int(input())
    if sec == 0:
        break
    c1 = int(input())
    c2 = int(input())
    c3 = int(input())
    vb = int(input())
    vn = int(input())
    eleicao[sec] = [c1, c2, c3, vb, vn]
    
for i in eleicao:
    c1_total += eleicao[i][0]
    c2_total += eleicao[i][1]
    c3_total += eleicao[i][2]
    vb_total += eleicao[i][3]
    vn_total += eleicao[i][4]   
v_total = c1_total + c2_total + c3_total + vb_total + vn_total
v_validos = c1_total + c2_total + c3_total

votos_totais = {'A': c1_total, 'B': c2_total, 'C': c3_total}
if c1_total == c2_total == c3_total:
    vencedor = ''
    quant_vencedor = 0
else:
    vencedor = max(votos_totais, key=votos_totais.get)
    quant_vencedor = votos_totais[vencedor]
    
print(f'Numero de votantes: {v_total}')
print(f'Total A: {c1_total}')
print(f'Total B: {c2_total}')
print(f'Total C: {c3_total}')
print(f'Brancos: {vb_total}')
print(f'Nulos: {vn_total}')
print(f'Validos: {v_validos}')
print(f'Candidato mais votado: {vencedor}')
print(f'Eleicao valida? {v_validos > (vb_total+vn_total)}')
print(f'Segundo turno? {quant_vencedor < v_validos*(50/100)}')
