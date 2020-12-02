def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO. Digite um número inteiro válido.\033[m')
            continue
        else:
            return num
