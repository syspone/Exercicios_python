# Exercicios em python (Lista)

# Ex1: Listas com multiplos valores
ms_list = [1, 2, "Maria", "Joao", 3, [1, 2, 3]]
print(ms_list)
'''
ms_list.pop()
print(ms_list) # excluindo ultimo elemento da lista

ms_list.sort()
print(ms_list) # typeError nao suporta str e int juntas
'''
# Dica extra para caso do sort
numeros = sorted([x for x in ms_list if isinstance(x, int)])
texto = sorted(x for x in ms_list if isinstance(x, str))
resultado = numeros + texto
print(resultado)