import random
import time
from Dados import *


# Parâmetros necessários para começar o jogo:
def main(dificuldade):
    global count
    global display
    global palavra
    global ja_ditas
    global tam
    global limite

    palavra = random.choice(palavras())
    tam = len(palavra)
    count = 0
    display = '_' * tam
    ja_ditas = []
    if dificuldade == 1:
        limite = 10
    elif dificuldade == 2:
        limite = 5
    else:
        limite = -1

    forca()


# Initializing all the conditions required for the game:
def forca():
    global count
    global display
    global palavra
    global ja_ditas
    global limite

    # palavra suxiliar que será alterada ao longo da rodada
    palavra_aux = palavra

    tentativa = input(f'A palavra é: {display}. Digite uma letra: \n').strip().lower()

    # Entrada inválida (símbolos, números, numero de caracteres inválido)
    if len(tentativa) == 0 or len(tentativa) >= 2 or tentativa.isnumeric():
        print("Caracter Inválido! Tente apenas uma letra.\n")
        forca()

    # Acertou a letra
    elif tentativa in palavra_aux:
        print('Você acertou!\n')
        ja_ditas.extend([tentativa])
        while True:  # substitui todas as letras iguais
            if tentativa in palavra_aux:
                index = palavra_aux.index(tentativa)
                palavra_aux = palavra_aux[:index] + '_' + palavra_aux[index + 1:]
                display = display[:index] + tentativa + display[index + 1:]
            else:
                break

    # Repetiu uma letra
    elif tentativa in ja_ditas:
        print("Você ja disse essa letra. Tente outra.\n")

    # Errou a letra
    else:
        ja_ditas.extend([tentativa])
        if limite == -1:  # Livre
            print('Letra errada. Tente Novamente.\n')
            forca()
        else:

            count += 1
            # Variável que diz qual desenho mostrar
            if limite == 5:
                des = count
            else:
                des = count / 2

            # Ainda existem tentativas restantes
            if count < limite:
                time.sleep(0.3)
                desenho(des)

                print("Letra Errada. " + str(limite - count) + " tentativas restantes.\n")

            # Você perdeu
            elif count == limite:
                time.sleep(0.3)
                desenho(des)
                print("Letra Errada. Você foi Enforcado!!!\n")
                print("A palavra era:", palavra)

    # Vitória
    if palavra == display:
        print("Parabéns! Você adivinhou a palavra!\n")
        quit()
    elif count != limite:  # Jogo continua
        forca()
