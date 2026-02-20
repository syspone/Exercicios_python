#!/usr/bin/env python3

import os
import sys
import subprocess


def montar_nome_arquivo(numero: int) -> str:
    return f"ex{numero}.py"


def executar_exercicio(numero: int) -> None:
    nome_arquivo = montar_nome_arquivo(numero)

    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        print("Crie o arquivo na mesma pasta deste script ou ajuste o padrão de nome.")
        return

    print(f"\n=== Executando {nome_arquivo} ===\n")
    try:
        subprocess.run([sys.executable, nome_arquivo], check=False)
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")
    except Exception as e:
        print(f"Erro ao executar '{nome_arquivo}': {e}")


def main() -> None:
    print("=== Runner de Exercícios em Python ===")
    print("Padrão de arquivos: ex<NÚMERO>.py (ex1.py, ex2.py, ...)")
    print("Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("Digite o número do exercício: ").strip().lower()

        if entrada in {"sair", "q", "quit", "exit"}:
            print("Encerrando.")
            break

        if not entrada.isdigit():
            print("Por favor, digite apenas o número do exercício (ex: 1, 2, 10).")
            continue

        numero = int(entrada)
        if numero <= 0:
            print("Use apenas números positivos (1, 2, 3, ...).")
            continue

        executar_exercicio(numero)
        print()  # linha em branco entre execuções


if __name__ == "__main__":
    main()

