def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError, NameError):
            print('ERRO : Digite um numero inteiro valido.')
        except(KeyboardInterrupt):
            print('Usuario preferiu não digitar o valor ')
        else:
            return num
            break


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except(ValueError, TypeError, NameError):
            print('RRo : Digite um numero real valido.')
        except(KeyboardInterrupt):
            print('Usuario preferiu não digitar valor ')
        else:
            return num
            break


def linha(tamanho):
    print('-' * tamanho)


def cabecalho(msg, tamanho):
    linha(tamanho)
    print(f'{msg:^{tamanho}}')
    linha(tamanho)


def menu(titulo,lista, tamanho=0):
    cabecalho(titulo,tamanho)
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    linha(tamanho)
    opc = leiaint('Sua opção:')
    return opc


def sim_ou_nao(msg):
    while True:
        resp = str(input(f'{msg}S/N')).split()
        if resp[0] in 'Nn':
            return False
        if resp[0] in 'SsYy':
            return True
        else:
            print('Digite uma opcao valida')
            continue