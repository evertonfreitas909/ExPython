#Desenvola um programa que leia seis números inteiros e mostre a soma apenas daqueles
#que forem pares. Se o valor digitado dor impar, desconsidere-o.
soma = 0
cont = 0
for c in range(1,  7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
    soma += num
    cont += 1
print('Você informou {} números e a soma foi {}'.format(cont, soma))
