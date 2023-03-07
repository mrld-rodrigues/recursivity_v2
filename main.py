import os
from time import sleep

"""
    # função recursiva, tem como objetivo imprimir uma pequena contagem de
    # encerramento do programa.
"""


def encerramento(n=1, perc=10):
    if n > 3:
        print("")
    else:
        if n == 1:
            print(f"\n...Apagando os registros...")
        elif n == 2:
            for a in range(1, 20):
                os.system('clear')
                print("\n")
                if perc == 100:
                    print("\tEncerrado!")
                    print("\n\tAgradecemos a sua utilização!\n"
                          "\tMelhores cumprimentos e bons hábitos sempre!!\n")
                else:
                    print("Fechando o programa...")
                    print("#" * (a + 12), perc, end="%")
                    a += 1
                    perc += 5
                    sleep(0.3)
        else:
            print("\n\t\t...Encerrando procedimentos...")
        sleep(1)
        return encerramento(n + 1)


encerramento()
