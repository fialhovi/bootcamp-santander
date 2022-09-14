# Estruturas Sequenciais:
idade = int(input('Digite sua idade: '))
print(f'Idade {idade}', type(idade))


print(float("123.25"),type(float('123.25')))
print(float("123.25"),type(str(123.24)))
print(bool(''))
print(bool('abc'))
print(bool(0))
print(bool(-2))


salario_mensal = float(input("Digite o valor do seu salário mensal: "))
gasto_mensal = float(input("Digite o valor do seu gasto mensal em média: "))

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12
montante_economizado = salario_total - gasto_total
print("O montante que você pode economizar ao fim do ano é de: ", montante_economizado)
