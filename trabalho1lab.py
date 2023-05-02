"""Jogo de dados: lançamento de dois dados e quem tiver o maior numero ganha a rodada, melhor de 5"""

import random as rd

rd.seed()

jogadas =0
num1=0
num2=0
começarojogo = input("Quer começar o jogo? [S/N]: ").upper()


if começarojogo == "S":

    while jogadas < 5 and num1 < 3 and num2 < 3:
        comecarrodada = input(f"Escreva 'Kafka' para começar a rodada {jogadas+1}: ").lower()
        if comecarrodada == "kafka":
        
            mao1= rd.randint(2,12)
            mao2= rd.randint(2,12)

            print("pontos do jogador 1: " , mao1)
            print("pontos do jogador 2: " , mao2)

            if mao1 == mao2:
                    
                mao3 = 0
                mao4 = 0
                while mao3 == mao4 :

                    mao3 = rd.randint(1,6)
                    mao4 = rd.randint(1,6)  

                    print("empate: novo lançamento de dados realizado: ")
                    print("pontos do jogador 1: ",  mao3)
                    print("pontos do jogador 2: ",  mao4)

                    if mao3 > mao4:
                        print("jogador 1 ganhou a rodada")
                        num1 += 1

                    if mao4 > mao3:
                        print("jogador 2 ganhou a rodada")
                        num2 += 1

            if mao1 > mao2:
                print("jogador 1 ganhou a rodada")
                num1 += 1

            if mao2 > mao1:
                print("jogador 2 ganhou a rodada")
                num2 += 1

            if num1 > num2:
                print("jogador 1 esta a ganhar:",num1, "-" , num2)

            if num2 > num1:
                print("jogador 2 esta a ganhar:",num1, "-", num2)
            
            if num1 == num2:
                print("o jogo esta empatado: ",num1, "-", num2)

            jogadas += 1

if começarojogo == "N":
    print("até a próxima!")
    exit()
        
if num1 > num2:
    print("jogador 1 ganhou!")

if num2 > num1:
    print("jogador 2 ganhou!")
    
    """wow que ganda trabalho tas de parabens ass: anonimos"""
