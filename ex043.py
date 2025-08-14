#Desenvolva uma lógica que leia o peso e altura deuma pessoa, calcule seu IMC e  mostre
#seu status, de acordo com a tabela abaixo:
#- abaixo de 18.5: Abaixo do peso
#- Entre 18.5 e 25: Peso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade mórbida

peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de peso normal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('Você está em obesidade!')
elif imc >= 40:
    print('Você está em obesidade mórbida, CUIDADO!')