#!/usr/bin/env python3

import os
import sys
import subprocess
import glob


def listar_arquivos_python() -> list[str]:
    """Lista todos os arquivos .py na pasta atual, exceto o próprio runner."""
    arquivos = []
    for arquivo in glob.glob("*.py"):
        if arquivo != os.path.basename(__file__):
            arquivos.append(arquivo)
    return sorted(arquivos)


def normalizar_nome_arquivo(entrada: str) -> str:
    """Normaliza o nome do arquivo, adicionando .py se necessário."""
    entrada = entrada.strip()
    if not entrada.endswith(".py"):
        entrada += ".py"
    return entrada


def buscar_arquivos(termo: str) -> list[str]:
    """Busca arquivos Python que contenham o termo no nome."""
    termo = termo.lower()
    todos_arquivos = listar_arquivos_python()
    return [arquivo for arquivo in todos_arquivos if termo in arquivo.lower()]


def buscar_por_numero(numero: str) -> list[str]:
    """Busca arquivos Python que contenham o número especificado no nome.
    
    Ex: "1" encontra "ex1.py", "exercicio1.py" mas não "ex10.py" ou "ex11.py"
    """
    import re
    todos_arquivos = listar_arquivos_python()
    encontrados = []
    
    # Padrão: número não precedido nem seguido por outro dígito
    # Usa lookahead e lookbehind negativo para garantir que não seja parte de número maior
    padrao = re.compile(r'(?<!\d)' + re.escape(numero) + r'(?!\d)')
    
    for arquivo in todos_arquivos:
        # Remove a extensão .py para buscar no nome
        nome_sem_ext = arquivo.replace(".py", "")
        if padrao.search(nome_sem_ext):
            encontrados.append(arquivo)
    
    return encontrados


def executar_arquivo(nome_arquivo: str) -> None:
    """Executa um arquivo Python."""
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        
        # Sugerir arquivos similares
        termo = nome_arquivo.replace(".py", "").lower()
        similares = buscar_arquivos(termo)
        
        if similares:
            print(f"\nArquivos similares encontrados:")
            for arquivo in similares:
                print(f"  - {arquivo}")
        else:
            print("\nArquivos Python disponíveis:")
            arquivos = listar_arquivos_python()
            if arquivos:
                for arquivo in arquivos:
                    print(f"  - {arquivo}")
            else:
                print("  (nenhum arquivo Python encontrado)")
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
    print("Digite o número do exercício (1, 2, 3...) ou o nome do arquivo")
    print("Comandos especiais:")
    print("  'listar' ou 'ls' - Lista arquivos disponíveis")
    print("  'sair', 'q', 'quit' ou 'exit' - Encerra o programa\n")

    while True:
        entrada = input("Digite o número do exercício: ").strip()

        if not entrada:
            continue

        entrada_lower = entrada.lower()

        # Comandos especiais
        if entrada_lower in {"sair", "q", "quit", "exit"}:
            print("Encerrando.")
            break

        if entrada_lower in {"listar", "ls", "list"}:
            arquivos = listar_arquivos_python()
            if arquivos:
                print("\nArquivos Python disponíveis:")
                for arquivo in arquivos:
                    print(f"  - {arquivo}")
            else:
                print("\nNenhum arquivo Python encontrado na pasta atual.")
            print()
            continue

        # Verificar se é apenas um número
        if entrada.isdigit():
            numero = entrada
            arquivos_encontrados = buscar_por_numero(numero)
            
            if not arquivos_encontrados:
                print(f"Nenhum arquivo encontrado com o número '{numero}'.")
                print("\nArquivos Python disponíveis:")
                arquivos = listar_arquivos_python()
                if arquivos:
                    for arquivo in arquivos:
                        print(f"  - {arquivo}")
                else:
                    print("  (nenhum arquivo Python encontrado)")
                print()
                continue
            
            # Se encontrou exatamente um arquivo, executar
            if len(arquivos_encontrados) == 1:
                executar_arquivo(arquivos_encontrados[0])
            else:
                # Se encontrou múltiplos, mostrar e executar o primeiro
                print(f"Encontrados {len(arquivos_encontrados)} arquivos com o número '{numero}':")
                for i, arquivo in enumerate(arquivos_encontrados, 1):
                    print(f"  {i}. {arquivo}")
                print(f"\nExecutando: {arquivos_encontrados[0]}")
                executar_arquivo(arquivos_encontrados[0])
        else:
            # Não é número, tentar executar como nome de arquivo
            nome_arquivo = normalizar_nome_arquivo(entrada)
            executar_arquivo(nome_arquivo)
        
        print()  # linha em branco entre execuções


if __name__ == "__main__":
    main()

