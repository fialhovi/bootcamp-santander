# Strings I
empresa = "Let's code"
print(empresa)
print()

#Usando o caractere de escape \ para não dar conflito
frase = "O Professor Pietro da Let's Code disse: \"Hoje a pizza é por minha conta\""
print(frase)
print()

#Método len():
tamanho = len(frase)
print("A frase possui", tamanho, "caracteres")

# Fatiando uma String:
empresa1 = 'Google'
print(f'Mostrando a letra na posição 0 do nome {empresa1}: {empresa1[0]}')

print(f'Mostrando as três primeiras letras do nome {empresa1}: {empresa1[:3]}')

# Método split para strings:
nomes_cidades = 'São Paulo, Belo Horizonte, Rio de Janeiro, Brasilia'
print(nomes_cidades[0]) # Antes do método split(', ') ele retorna somente a primeira letra 's' da cidade de são paulo
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)
print(nomes_cidades[0]) # Usando o método split ele retorna o nome da cidade de São Paulo
print(nomes_cidades[1])
print()

# Método strip():
cabecalho = '               MENU PRINCIPAL          '

# Sem o método strip():
print(f'Sem o método strip(): {cabecalho}')

# Com o método strip():
print(f'Com o método strip(): {cabecalho.strip()}')
print()

# Métodos: title(), capitalize(), lower(), upper():
cidade = 'rIo dE JaNeiRo'
print(f'Usando o Método title(): {cidade.title()}')
print(f'Usando o Método capitalize(): {cidade.capitalize()}')
print(f'Usando o Método lower(): {cidade.lower()}')
print(f'Usando o Método upper(): {cidade.upper()}')
print()

# Exercicio:
nome_cidade = input('Qual cidade do Brasil é conhecida como cidade maravilhosa?  ').strip()
while nome_cidade.lower() != 'rio de janeiro':
    print('Tenta de novo aí...')
    nome_cidade = input('Qual cidade do Brasil é conhecida como cidade maravilhosa?  ').strip()
print('Boa Campeão!! ')

# Podemos converter strings para listas:
listafrase = list(frase)
print(f'Podemos converter strings para listas: {listafrase}')

# A função join() intercala cada elemento de uma lista com uma string.
stringfinal = '-py'.join(listafrase)
print(stringfinal)
print()

# Usar um join() com uma string vazia é útil para transformar a lista de volta
# em string:
stringfinal = ''.join(listafrase)
print(stringfinal)

# Podemos inserir quebras de linha com '\n'
frase = 'uma\nFRASE'
print(frase)

# Podemos inserir tabulação com '\t'
frase = 'uma\n\tFRASE'
print(frase)

# Para conseguir representar a barra '\', precisamos de 2 barras:
frase = 'uma\\FRASE'
print(frase)


# Strings II

# Operador + em string:
cumprimento = 'Olá, '
nome = 'Felipe'
print(cumprimento + nome)

# operador * em string:
print(nome * 5)

idade = 35
n_filhos = 2

# Método format():
print('{} tem {} anos e {} filhos'.format(nome, idade, n_filhos))
print()

# Formatando numeros:
preco_gasolina = 3.476
print('O preço da gasolina subiu e está em R$ {:.2f}'.format(preco_gasolina))
#O f é uma flag indicando que é float; o 2 indica que só vai até duas casas decimais
#Importante considerar que ele arredonda o valor, nesse caso, 3.48

# Método f em string:
print(f'{nome} tem {idade} anos e {n_filhos} filhos ')

#
dia = 1
mes = 8
ano = 2019
data1 = '{}/{}/{}'.format(dia, mes, ano)
print(data1)
# Saída: 1/8/2019
# O dia e o mês ocupam apenas um espaço

data2 = '{:2d}/{:2d}/{:4d}'.format(dia, mes, ano)
# A opção 'd' significa que o parâmetro é um número inteiro.
print(data2)
# Saída:  1/ 8/2019
# Agora, dia e mês ocupam obrigatoriamente 2 espaços:  1/ 8/2019


# Podemos forçar que os espaços em branco sejam preenchidos com o número 0:
data3 = '{:02d}/{:02d}/{:04d}'.format(dia, mes, ano)
print(data3)
# Saída: 01/08/2019
# Agora sim a data está no formato usual, dd/mm/aaaa: 01/08/2019

#Utilizando o format
nome = "Vinícius"
idade = 26
salario = 6000.40
print(f'{nome} tem {idade} anos e o salario: {salario:.2f}.')
