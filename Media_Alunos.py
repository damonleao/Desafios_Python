while True:

    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    n4 = float(input("Digite a nota 4: "))

    media = (n1 + n2 + n3 + n4) / 4

    print("Média:", media)

    if media >= 6:
        print("ALUNO APROVADO! PARABÉNS!!!")
    elif media > 4 and media < 6:
        print("ALUNO EM RECUPERAÇÃO! APROVEITE BEM A NOVA OPORTUNIDADE!")
    else:
        print("ALUNO REPROVADO! ESTUDE MAIS!")

    continuar = input("Deseja continuar? (s/n): ")

    if continuar == "n":
        break

