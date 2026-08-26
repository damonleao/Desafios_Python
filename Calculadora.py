while True:
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 5:
        break

    if opcao < 1 or opcao > 4:
        print("Opção inválida!")
        continue

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print("Resultado:", n1 + n2)

    elif opcao == 2:
        print("Resultado:", n1 - n2)

    elif opcao == 3:
        print("Resultado:", n1 * n2)

    elif opcao == 4:
        print("Resultado:", n1 / n2)

