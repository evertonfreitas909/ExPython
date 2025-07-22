#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
from ex012 import preço

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.')
'''if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45''' # uma maneira de fazer
preço = distância * 0,50 if distância <= 200 else distância * 0,45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
