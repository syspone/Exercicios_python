# Resolução:

# Descobri se o numero e par digitado e par ou impar

# O Python calcula: 6 % 2, que resulta em 0.
# Depois ele compara: 0 == 0? Sim!

numero = int(input("Digite um numero inteiro: "))

if numero % 2 == 0:
    print("o numero e Par.")
else:
    print("o numero e impar.")