import pickle

# Questão 1
def questao_1():
    with open("arq.txt", "w") as arq:
        while True:
            resposta = input("Digite um caractere (ou 0 para parar): ")
            if resposta == "0":
                break
            arq.write(resposta)
    with open("arq.txt", "r") as arq:
        conteudo = arq.read()
        print("Conteúdo do arquivo:", conteudo)

# Questão 2
def questao_2():
    arquivo = input("Digite o nome do arquivo: ")
    try:
        with open(arquivo, "r") as arq:
            linhas = arq.readlines()
            print(f"O arquivo possui {len(linhas)} linhas.")
    except FileNotFoundError:
        print("Arquivo não encontrado!")

# Questão 3
def questao_3():
    arquivo = input("Digite o nome do arquivo: ")
    vogais = "aeiouAEIOU"
    contador = 0
    try:
        with open(arquivo, "r") as arq:
            for linha in arq:
                for letra in linha:
                    if letra in vogais:
                        contador += 1
        print(f"O arquivo contém {contador} vogais.")
    except FileNotFoundError:
        print("Arquivo não encontrado!")

# Questão 4
def questao_4():
    arquivo = input("Digite o nome do arquivo: ")
    caractere = input("Digite o caractere a ser contado: ")
    contador = 0
    try:
        with open(arquivo, "r") as arq:
            for linha in arq:
                contador += linha.count(caractere)
        print(f"O caractere '{caractere}' ocorre {contador} vezes no arquivo.")
    except FileNotFoundError:
        print("Arquivo não encontrado!")

# Questão 5
def questao_5():
    arquivo_origem = input("Digite o nome do arquivo de origem: ")
    arquivo_destino = input("Digite o nome do arquivo de destino: ")
    try:
        with open(arquivo_origem, "r") as origem:
            conteudo = origem.read()
        with open(arquivo_destino, "w") as destino:
            destino.write(conteudo.upper())
        print(f"Conteúdo convertido e salvo em '{arquivo_destino}'.")
    except FileNotFoundError:
        print("Arquivo de origem não encontrado!")

# Questão 6
def questao_6():
    arquivo = input("Digite o nome do arquivo: ")
    palavra = input("Digite a palavra a ser contada: ")
    contador = 0
    try:
        with open(arquivo, "r") as arq:
            for linha in arq:
                contador += linha.split().count(palavra)
        print(f"A palavra '{palavra}' aparece {contador} vezes no arquivo.")
    except FileNotFoundError:
        print("Arquivo não encontrado!")

# Questão 7
def questao_7():
    with open("cadastro.txt", "w") as arq:
        while True:
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone (ou 0 para encerrar): ")
            if telefone == "0":
                break
            arq.write(f"{nome},{telefone}\n")
    print("Cadastro concluído.")

# Questão 8
def questao_8():
    arquivo = input("Digite o nome do arquivo de produtos: ")
    total = 0.0
    try:
        with open(arquivo, "r") as arq:
            for linha in arq:
                _, preco = linha.rsplit(",", 1)
                total += float(preco)
        print(f"Total da compra: R$ {total:.2f}")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except ValueError:
        print("Erro no formato do arquivo!")