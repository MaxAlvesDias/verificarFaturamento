import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

menorFaturamento = min(faturamentos)

maiorFaturamento = max(faturamentos)

mediaMensal = sum(faturamentos) / len(faturamentos)

diasAcimaDaMedia = len([f for f in faturamentos if f > mediaMensal])

print(f"Menor faturamento: {menorFaturamento}")
print(f"Maior faturamento: {maiorFaturamento}")
print(f"Dias com faturamento acima da média: {diasAcimaDaMedia}")
