#Crie um programa que leia o nome de uma cidade e diga se la começa ou não com o nome "Santo"
cid = str(input('Qm que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'Santo')