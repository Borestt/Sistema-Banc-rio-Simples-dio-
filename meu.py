menu = ''' -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[0] - Depositar
[1] - Sacar
[2] - Extrato
[3] - Sair

Escolha sua opção
==> '''

saldo = 0
extrato = ""

while True:
    opcao = int(input(menu))

    if opcao == 0:
        valor = float(input("Digite o valor do deposito: "))
        print()

        if valor > 0:
            saldo += valor
            extrato += f"Foi depositado {valor:.2f}\n"

    if opcao == 1:
        valor = float(input("Digite o valor do saque (limite de R$500): "))
        print()
        if valor <= 500:
            saldo -= valor
            extrato += f"Foi sacado {valor:.2f}\n"
        else:
            print("Saldo acima do limite\n")
    if opcao == 2:
        print("EXTRATO".center(35, '='))
        print("Não houve movimentações" if not extrato else extrato) 
        print(f'Saldo R$:{saldo:.2f}')
        print("EXTRATO".center(35, '='))
    if opcao == 3:
        break
    else:
        print('Opção inválida!')
