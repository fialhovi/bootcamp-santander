valor_passagem = 4.30
valor_corrida = float(input("Qual é o valor da corrida? "))

if valor_corrida <= valor_passagem * 5:
    print('Pague a corrida')
else:
    print('Pegue o ônibus')



valor_passagem = 4.30
valor_corrida = float(input("Qual é o valor da corrida? "))

if valor_corrida <= valor_passagem * 5:
    print('Pague a corrida')
elif valor_corrida <= valor_passagem * 6:
    print('Aguarde alguns minutos e verifique novamente o preço do Uber')
else: 
    print("Pegue o ônibus")
