
valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário do comprador: R$ "))
anos = int(input("Em quantos anos deseja pagar? "))

meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30

print("Valor da prestação mensal: R$", prestacao)
print("Limite máximo (30% do salário): R$", limite)

if prestacao <= limite:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO! A prestação excede 30% do salário.")
