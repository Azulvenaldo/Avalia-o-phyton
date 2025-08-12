
saldo = 200.0

while True:
    print("1. Consultar saldo")
    print("2. Depositar dinheiro")
    print("3. Sacar dinheiro")
    print("4. Sair")
    opcao =input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "2":
        valor = float(input("Valor para deposito: "))
        saldo += valor
    elif opcao == "3":
        valor = float(input("Valor para saque: "))
        if valor <= saldo:
            saldo -= valor
        else:
            print("Saldo insuficiente. ")
    elif opcao == "4":
        break
    else:

        print("Opção invalida. ")
