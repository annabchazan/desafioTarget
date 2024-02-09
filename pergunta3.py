import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

valores_nao_nulos = [item['valor'] for item in dados if item['valor'] != 0]


if len(valores_nao_nulos) != 0:
    media_faturamento = sum(valores_nao_nulos) / len(valores_nao_nulos)
else:
    media_faturamento = 0

menor_valor = float('inf')
maior_valor = -1
qtt = 0

for elemento in dados:
    valor_atual = elemento['valor']


    if valor_atual != 0 and valor_atual < menor_valor:
        menor_valor = valor_atual

    if valor_atual > maior_valor:
        maior_valor = valor_atual


    if valor_atual > media_faturamento:
        qtt += 1

if menor_valor != float('inf'):
    print(f"O menor valor de faturamento em um mês é, desconsiderando finais de semana e feriados: {menor_valor}")

print(f"O maior valor de faturamento em um mês é: {maior_valor}")
print(f"Número de vendas com faturamento diário maior à média mensal: {qtt}")
