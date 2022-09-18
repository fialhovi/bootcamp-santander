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





#QUESTÃO 2
#Faça um programa que peça para o usuário digitar uma palavra e imprima
#cada letra em uma linha.


palavra = str(input('Digite uma palavra:\n'))

for index in range(len(palavra)):
    print(palavra[index])
    

    
    
    
#QUESTÃO 3
#Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.
#Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].


def soma_lista(lista1, lista2):
    soma = [x + y for x, y in zip(lista1, lista2)]
    return soma
    
soma_lista([1,4,3], [3,5,1])





#QUESTÃO 4
#
