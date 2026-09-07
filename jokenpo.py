import random
import time

print("=== JOKENPÔ ===")
print("[ 0 ] Pedra")
print("[ 1 ] Papel")
print("[ 2 ] Tesoura")

escolha_jogador = int(input("Qual é a sua jogada? "))

escolha_computador = random.randint(0, 2)

print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
print("-=" * 11)

if escolha_computador == 0:
    print("Computador jogou: Pedra")
else:
    if escolha_computador == 1:
        print("Computador jogou: Papel")
    else:
        print("Computador jogou: Tesoura")

if escolha_jogador == escolha_computador:
    print("EMPATE!")
else:
    if escolha_jogador == 0 and escolha_computador == 2:
        print("VOCÊ GANHOU! Pedra ganha de Tesoura")
    else:
        if escolha_jogador == 1 and escolha_computador == 0:
            print("VOCÊ GANHOU! Papel ganha de Pedra")
        else:
            if escolha_jogador == 2 and escolha_computador == 1:
                print("VOCÊ GANHOU! Tesoura ganha de Papel")
            else:
                print("VOCÊ PERDEU!")
