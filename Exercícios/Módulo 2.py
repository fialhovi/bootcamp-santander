#QUESTÃO 1
#Faça um programa que olhe todos os itens de uma lista e diga quantos deles
#são pares.


numeros = [0,1,2,3,45,46,47,52,68,236,241,528]
print(numeros)


pares = []
for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)

print(len(pares))







