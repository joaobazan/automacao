#Uma empresa pediu para você criar um programa para calcular um bônus ao seus funcionários. A regra é a seguinte: Do faturamento total da empresa, os funcionários receberão 10% de bônus. Gire um código que calcule esse bônus.
#Faturamento total da empresa: R$ 50.000,00
#Bônus: 10%
#No final mostre o faturamento inicial, o valor do bônus e o faturamento após o bônus.

faturamento = 50000
bonus = faturamento * 0.10
faturamentofinal = faturamento - bonus
print(f"O faturamento inicial {faturamento}, bônus {bonus}, O faturamento final é {faturamento}")