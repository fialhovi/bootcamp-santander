#QUESTÃO 1
#Faça um programa que peça um valor monetário e diminua-o em 15%. 
#Seu programa deve imprimir a mensagem "O novo valor é [valor]".


valor = float(input('Informe o valor monetário:'))
print ("O novo valor é ", valor * 0.85)





#QUESTÃO 2
#Faça um programa que leia a validade das informações:
#a. Idade: entre 0 e 150;
#b. Salário: maior que 0;
#c. Sexo: M, F ou Outro;
#O programa deve imprimir uma mensagem de erro para cada informação inválida.


idade = int(input('Qual é a sua idade?'))
if int(idade) < 0 or int(idade) > 150:
    print('Campo Idade preenchido incorretamente.')

salario = float(input('Qual é o seu salário'))
if float(salario) < 0:
    print('Campo Salário preenchido incorretamente.')

sexo = str(input('Qual o seu sexo (M, F, Outro)?'))
if str(sexo) != 'M' or str(sexo) != 'F' or str(sexo) != 'Outro':
    print('Campo Sexo preenchido incorretamente.')





#QUESTÃO 3
#Vamos fazer um programa para verificar quem é o assassino de um crime.
#Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:
    
    #a. Mora perto da vítima?
    #b. Já trabalhou com a vítima?
    #c. Telefonou para a vítima?
    #d. Esteve no local do crime?
    #e. Devia para a vítima?
    
#Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
#suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
#2 pontos são apenas suspeitos, necessitando outras investigações. Valores
#iguais ou abaixo de 1 são liberados.


pergunta1 = str(input('Mora perto da vítima? True or False.'))
pergunta2 = str(input('Já trabalhou com a vítima? True or False.'))
pergunta3 = str(input('Telefonou para a vítima? True or False.'))
pergunta4 = str(input('Esteve no local do crime? True or False.'))
pergunta5 = str(input('Devia para a vítima? True or False.'))
ponto_suspeito = 0

if pergunta1 == "True":
    ponto_suspeito = ponto_suspeito + 1
if pergunta2 == "True":
    ponto_suspeito = ponto_suspeito + 1
if pergunta3 == "True":
    ponto_suspeito = ponto_suspeito + 1
if pergunta4 == "True":
    ponto_suspeito = ponto_suspeito + 1
if pergunta5 == "True":
    ponto_suspeito = ponto_suspeito + 1

if ponto_suspeito == 5:
    print('Pontos de suspeita: ', ponto_suspeito)
    print('Assassino')
if ponto_suspeito == 4 or ponto_suspeito == 3:
    print('Pontos de suspeita: ', ponto_suspeito)
    print('Cúmplice')
if ponto_suspeito == 2:
    print('Pontos de suspeita: ', ponto_suspeito)
    print('Suspeito')
if ponto_suspeito == 1 or ponto_suspeito == 0:
    print('Pontos de suspeita: ', ponto_suspeito)
    print('Liberado')




#QUESTÃO 4
#Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.


contador = 0
while contador <= 9:
    contador = contador + 1
    print('9 *', contador, '= ', 9 * contador)
print('Fim da tabuada do 9')
