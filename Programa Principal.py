
from time import sleep
from Jogo import main
from leiaInt import leiaint

# Boas Vindas:
print('\nJogo da Forca by William Gliz\n')
nome = input("Digite seu nome: ")
print(f'Olá {nome}! Lhe desejo Boa Sorte!\n')
sleep(0.5)
print("O jogo já vai Começar!\n")
sleep(0.5)

# Seleção de dificuldade:
print("""Dificuldades:
1 - Facil   - 10 tentativas
2 - Dificil - 5 tentativas
3 - Livre   - Sem limite de tentativas """)

dificuldade = leiaint('Escolha a dificuldade: ')
print()

jogar = True

while jogar:
    main(dificuldade)

    sleep(0.5)
    resp = str(input('Quer jogar novamente?')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Quer jogar novamente?')).strip().lower()[0]
    if resp == 'n':
        jogar = False

sleep(0.2)
print('\nObrigado por jogar! Volte Sempre!')
