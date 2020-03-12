import random 
import os 

cartas  = ["A", "2", "3", "4","5", "6","7", "8", "9","10","J", "Q","K"]*4
def baralho(cartas):
    mao = []
    for i in range (len(cartas)):
        random.shuffle(cartas)
        carta = cartas.pop()
        mao.append(carta)
    return mao
def nova_jogada():
    nova = input("deseja fazer nova jogada ? (s/n").upper()
    if nova == "y":
        dealer = []
        jogador = []
        cartas  = ["A", "2", "3", "4","5", "6","7", "8", "9","10","J", "Q","K"]*4
        jogo()
    else:
        print("Acabou!")
        pass
def pontos(mao):
    total = 0
    for carta in mao:
        if carta == "J" or carta == "Q" or carta "K":
            total+=10





c = baralho(cartas)
print(c)






    
