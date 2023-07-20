menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(' BANCO AZEVEDO '.center(40, '-'))
    opcao = input(menu)

    if opcao == "d":
        print(" Depósito ".center(20, '-'))
        deposito = float(input('Informe o valor a ser depositado: R$'))
        if deposito > 0:
            saldo += deposito
            extrato += (f'Depósito: R${deposito:.2f}\n')
            print(f'DEPÓSITO REALIZADO COM SUCESSO!')
        else:
            print('VALOR INVÁLIDO!')


    elif opcao == "s":
        print(" Saque ".center(20, '-'))
        print(f'Saldo: R${saldo}')
        saque = float(input('Informe o valor a ser sacado: R$'))
        if saque > 0:
            if saque <= saldo and saque <= 500 and LIMITE_SAQUES > 0:
                saldo -= saque
                LIMITE_SAQUES -= 1
                print(f'SAQUE REALIZADO COM SUCESSO!')
                extrato += (f'Saque: R${saque:.2f}\n')
            elif saque > saldo:
                print(f'Saldo insuficiente!')
            elif LIMITE_SAQUES == 0:
                print('SAQUE NÃO EFETUADO! Limite de operação diária excedida.')
            elif saque > 500:
                print('SAQUE NÃO EFETUADO! Limite por operação até R$500,00')
        else:
             print('VALOR INVÁLIDO!')   


    elif opcao == "e":
        print(" Extrato ".center(20, '-'))
        print(f'Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')

    elif opcao == "q":
        print('OBRIGADA POR USAR O BANCO AZEVEDO! VOLTE SEMPRE!')
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    print('-='*20)