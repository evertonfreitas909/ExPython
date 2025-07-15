#Faça um programa que leia o cumprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o cumprimento da hipotenusa.
'''co = float(input('Cumprimanto do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
# ** (1/2) significa elevar ao quadrado
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

'''import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi)'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))