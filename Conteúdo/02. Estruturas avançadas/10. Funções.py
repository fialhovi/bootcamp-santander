# Funções:

# Declarando uma função sem parêmetro:
def hello():
    print('Olá, Mundo!')


hello()


# Declarando uma função com parâmetro que calcula a média aritmética de três notas:
def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

nota = calcula_media(8.5, 4.9, 10)
print(f'Média: {nota}')


# Funções recursivas:

def funcaoRecursiva(numero):
    if (numero != 1):
        funcaoRecursiva(numero - 1)
    print(numero)

print("Testando a função recursiva:")
funcaoRecursiva(10)



# Funções II

# Funções com varios parâmetros: quando utilizamos um * em parâmetros, quer dizer que podemos passar vários argumentos, que são armazenados em
# uma tupla().
def calcula_media1(*args):
    soma = sum(args)
    media = soma / len(args)
    return media

print(f'Média de vários parâmetros: {calcula_media1(10, 5, 8, 9, 10, 7, 6, 2)}')


# Funções com vários parâmetros: quando utilizamos dois ** em parâmetros, quer dizer que podemos passar vários argumentos, que são armazenados em
# um dicionario().
def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome='Vinícius', sobrenome='Fialho')
