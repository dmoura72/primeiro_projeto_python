menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
num_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Informe o valor para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Operação realizada com sucesso! Seu saldo atual:  R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "s":

        valor = float(input("Informe o valor do saque: "))

        exedeu_saldo = valor > saldo
        execeu_limite = valor > limite
        execeu_saques = num_saque >= LIMITE_SAQUE

        if exedeu_saldo:
            print("Operação falou! Saldo insuficiente.")

        elif execeu_limite:
            print("Operação falou! Saldo insuficiente.")

        elif execeu_saques:
            print("Operação falhou! Valor linite de saque excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saque += 1
            print(f"Operação realizada com sucesso! Seu saldo atual:  R$ {saldo:.2f}\n")

        else:
            print("Operação falhou! Ovalor informado é inválido")

    elif opcao == "e":
        print("\n=====================EXTRATO====================")
        print(f"Não foram realizadas operações." if not extrato else extrato)
        print(f"Saldo = R$ {saldo:.2f}")
        print("==================================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida! Por favor selecione uma das opções válidas.")


    