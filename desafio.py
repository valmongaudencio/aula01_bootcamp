CONSTANTE_BONUS = 1000

nome = input("Digite seu nome: ")

salario = float(input("Digite seu salário: "))

perc = float(input("Digite o percentual de bônus: "))

# Convertendo o percentual para decimal
perc_decimal = perc / 100

bonus = CONSTANTE_BONUS + salario * perc_decimal

print(f"O bônus de {nome} é de R${bonus:.2f}")

