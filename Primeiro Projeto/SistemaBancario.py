menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
contador_extrato = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(' BANCO AZEVEDO '.center(40, '-'))
    print(f'SALDO DA CONTA: R${saldo}')
    opcao = input(menu)

    if opcao == "d":
        print(" Depósito ".center(20, '-'))
        print(f'Saldo: R${saldo}')
        deposito = float(input('Informe o valor a ser depositado: R$'))
        if deposito > 0:
            saldo += deposito
            contador_extrato += 1
            extrato += (f'{contador_extrato} - Operação: Depósito \nValor: +R${deposito:.2f} \nSaldo:R${saldo:.2f}\n\n')
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
                contador_extrato += 1
                extrato += (f'{contador_extrato} - Operação: Saque \nValor: -R${saque:.2f} \nSaldo:R${saldo:.2f}\n\n')
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
        print(extrato)

    elif opcao == "q":
        print('OBRIGADA POR USAR O BANCO AZEVEDO! VOLTE SEMPRE!')
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    print('-='*40)