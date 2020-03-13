import random 
import os 
cartas  = ["A", "2", "3", "4","5", "6","7", "8", "9","10","J", "Q","K"]
naipes = ['♥','♦','♣','♠']
mao = []
mao_jogador = []
def inicio():
    for i in naipes:
        for j in cartas:
            
            mao.append("{}{}".format(j, i))
    return mao
          

def embaralhar(mao):
    mao = random.shuffle(mao)
    return mao




def hit(mao):
    card = random.choice(mao)
    mao_jogador.append(card)
    mao.remove(card)
    return mao_jogador

def nova_jogada(mao_jogador, mao):
    nova = input('nova jogada ? s/n ? ')
    if nova == "s":
        mao_dealer=[]
        mao_jogador=[]
        cartas  = ["A", "2", "3", "4","5", "6","7", "8", "9","10","J", "Q","K"]
        naipes = ['♥','♦','♣','♠']
        jogo()
    else:
        print("Até a proxima! ")
        exit()

        
        

def pontos(mao):
    total= 0
    for carta in mao:
        if carta == "J" or carta == "Q" or carta == "K" or carta == "10":
            total+=10
        elif carta == "9":
            total += 9
        elif carta == "8":
            total += 8
        elif carta == "7":
            total += 7
        elif carta == "6":
            total += 6
        elif carta == "5":
            total += 5
        elif carta == "4":
            total += 4
        elif carta == "3":
            total += 3
        elif carta == "2":
            total += 2
        elif carta == "A":
            if total >= 11: total += 1
        else: total += 11
    return total

def limpar():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def resultados(mao_dealer, mao_jogador):
    limpar()
    print("a mesa tem"+str(mao_dealer)+"para"+ str(total(mao_dealer)))
    print("voce tem"+ str(mao_jogador)+ "para"+str(total(mao_jogador)))

if __name__ == "__main__":
   game()


        


        
    
    














    
