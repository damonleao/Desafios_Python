print("=== SISTEMA DE CADASTRO ===")

while True:

    nome = input("Digite seu nome: ")

    altura = float(input("Digite sua altura: "))

    salario = float(input("Digite seu salário: "))

    estudante = input("Você é estudante? (S/N): ")

    print("\n=== DADOS CADASTRADOS ===")
    print("Nome:", nome)
    print("Altura:", altura)
    print("Salário:", salario)

    if estudante.lower() == "s":
        print("Estudante: Sim.")
    elif estudante.lower() == "n":
        print("Estudante: Não.")
    else:
        print("Resposta inválida. Digite S ou N.")

    continuar = input("\nDeseja cadastrar outra pessoa? (S/N): ")

    if continuar.lower() == "n":
        print("Programa encerrado.")
        break

    print()
