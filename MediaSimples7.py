# 1. Constante (por convenção, usamos MAIÚSCULAS)
MEDIA_MINIMA = 7.0

# 2. Variáveis (Entrada de dados)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 3. Processamento
media_final = (nota1 + nota2) / 2

print(f"Sua média foi: {media_final}")

# 4. Lógica de Decisão
if media_final >= MEDIA_MINIMA:
    print("Resultado: APROVADO! 🎉")
else:
    print("Resultado: REPROVADO. Precisa estudar mais! 📚")
