def palavras():
    palavras = ['amanha', 'janeiro', 'hoje', 'filme', 'plantas', 'cachorro', 'papagaio', 'cadeira',
                'jornal', 'amanhecer', 'escritorio']
    return palavras


def desenho(cont=0):
    if cont <= 1:
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif cont <= 2:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif cont <= 3:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif cont < 5:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |      \n"
              "__|__\n")
    elif cont == 5:
        print("   _____   \n"
              "  |     |  \n"
              "  |     |  \n"
              "  |     O  \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")

