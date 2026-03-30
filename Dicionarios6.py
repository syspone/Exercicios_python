# Considere o dicionário abaixo para responder a pergunta:
# Caso queira retornar os pares chave e valor do dicionário, qual é a maneira correta de realizar esse procedimento?

meu_dicionario = {
    "registro": "0001",
    "produto": "notebook",
    "modelo": "Macbook",
    "conexões": ["usb-c", "usb", "p2", "hdmi"]
}

print(meu_dicionario.items())

# Se for necessário adicionar mais um elemento ao dicionário, referente aos itens periféricos,
# .....mouse e teclado, que acompanham o produto, qual das alternativas abaixo representa corretamente como deve ser feito esse procedimento?

meu_dicionario["perifericos"] = ["mouse", "teclado"]
print(meu_dicionario)

# Caso queira retornar somente as chaves do dicionário, qual é a maneira correta de realizar esse procedimento?

print(meu_dicionario.keys())

# Caso queira retornar somente os valores do dicionário, qual é a maneira correta de realizar esse procedimento?

print(meu_dicionario.values())