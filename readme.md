# Exercícios em Python

Este projeto contém exercícios em Python. A execução é feita sempre pelo **runner**, que identifica automaticamente os números nos nomes dos arquivos e permite executar apenas digitando o número do exercício.

---

## Como executar

### 1. Abrir o runner

No terminal, na pasta do projeto, execute:

```bash
python3 run_exercicios.py
```

(Se o comando `python` no seu sistema já for o Python 3, pode usar `python run_exercicios.py`.)

### 2. Digitar o número do exercício

Quando aparecer a mensagem:

```
Digite o número do exercício:
```

Você pode:

- **Digitar apenas o número**: `1`, `2`, `3` (o runner encontra automaticamente arquivos como `ex1.py`, `formatacao2.py`, `exercicio3.py`, etc.)
- **Digitar o nome completo do arquivo**: `ex1.py`, `formatacao2.py` (com ou sem extensão `.py`)

O runner identifica números nos nomes dos arquivos. Por exemplo:
- Digitar **`1`** executa arquivos como `ex1.py`, `exercicio1.py`, `teste1.py`
- Digitar **`2`** executa arquivos como `ex2.py`, `formatacao2.py`, `aula2.py`

**Importante:** O runner busca o número exato. Por exemplo, digitar `1` encontra `ex1.py` mas **não** encontra `ex10.py` ou `ex11.py`.

Pressione **Enter** para executar.

### 3. Comandos especiais

O runner possui alguns comandos úteis:

- **`listar`**, **`ls`** ou **`list`**: Lista todos os arquivos Python disponíveis na pasta
- **`sair`**, **`q`**, **`quit`** ou **`exit`**: Encerra o programa

---

## Exemplos de uso

```
Digite o número do exercício: 1
=== Executando ex1.py ===
Hello, World!

Digite o número do exercício: 2
=== Executando formatacao2.py ===
...

Digite o número do exercício: listar
Arquivos Python disponíveis:
  - ex1.py
  - formatacao2.py

Digite o número do exercício: sair
Encerrando.
```

---

## Resumo

| Ação              | Comando / Comportamento                                    |
|-------------------|------------------------------------------------------------|
| Iniciar o runner  | `python3 run_exercicios.py`                                |
| Rodar exercício   | Digitar o número (1, 2, 3...) ou nome do arquivo e Enter  |
| Listar arquivos   | Digitar `listar`, `ls` ou `list` e Enter                   |
| Encerrar          | Digitar `sair`, `q`, `quit` ou `exit` e Enter              |

**Importante:** não execute os arquivos Python diretamente. Use sempre o `run_exercicios.py` e, quando solicitado, digite o número do exercício ou o nome do arquivo que deseja executar.
