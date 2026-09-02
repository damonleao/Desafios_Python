notas = []
aprovados = 0
reprovados = 0

for i in range(10):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1

maiornota = max(notas)
menornota = min(notas)
media = sum(notas) / len(notas)

print("\n=== RESULTADO ===")
print("Maior nota:", maiornota)
print("Menor nota:", menornota)
print(f"Média: {media:.2f}")
print("Aprovados:", aprovados)
print("Reprovados:", reprovados)
