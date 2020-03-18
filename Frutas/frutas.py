# O jogo deverá sortear uma fruta conforme a lista abaixo:
# - banana
# - jabuticaba
# - pitanga
# - mirtilo
# - morango
# - abacaxi
# - cereja
# O objetivo é acertar o nome da fruta. O jogador informa uma letra e o jogo verifica se a fruta tem essa letra.

import random
lista_frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'morango', 'abacaxi', 'cereja']
fruta_sorteada = random.choice(lista_frutas)

lista_escolha=[]
string=''

for i in fruta_sorteada:
    lista_escolha.append(i)
print(lista_escolha)
lista_letra=[]
for i in lista_escolha:
    lista_letra.append('_')
continua = True

while continua :
    letra = input("Digite uma letra: \n")
    try:
        i = int(letra)
        print ("apenas letras!\n")
    except ValueError:
        if len(list(letra)) > 1:
            print('digitar uma letra apenas')
            continue
        if letra in lista_escolha:
            print('pertence\n')
            for i in range(len(lista_escolha)):
                if letra in lista_escolha[i]:
                    lista_letra[i]=letra
            print(" ".join(lista_letra))
            print('')
        else:
            print(f'{letra} não pertence a fruta')
            print('', lista_letra)
        if "_" not in lista_letra:
            print('vc ganhou !!\n')
            continua=False






