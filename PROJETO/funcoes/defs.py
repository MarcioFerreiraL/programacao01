import time
def linhasF(frase):
    quantidadeTracos = len(frase)
    print('-' * (quantidadeTracos + 14))
    print(f'  {frase.upper().center(len(frase) + 10)} ')
    print('-' * (quantidadeTracos + 14))
    return quantidadeTracos

def linhas():
    print('-' * (28))

def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt', encoding='utf-8')
    except:
        return False
    else:
        return True
    finally:
        arquivo.close()
    
def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+', encoding='utf-8')
    except:
        print('Houve um ERROR na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso!')
    finally:
        arquivo.close()

def procurar_carro(nome):
    resultado = []
    try:
        arquivo = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo.')
    else:
        for dado in arquivo:
            dado = dado.replace('\n', '')
            dado = dado.split(',')  
            resultado.append([dado[0], dado[1], dado[2], dado[3]])        
        if not resultado:
            print("Carro não encontrado!")
        else: 
            return resultado
    finally:
        arquivo.close()

def buscarCarros(arquivo):
    resultado = []
    print("Informe um valor numérico se deseja buscar por preço máximo ou uma palavra se deseja buscar pelo estado do carro (por exemplo: 'novo', 'seminovo', 'conservado', 'mal estado'):")
    pesquisa = input()
    carros = procurar_carro(arquivo)
    time.sleep(1)
    if pesquisa.isnumeric() == True:
        for carro in carros:
            if float(carro[1]) < float(pesquisa):
                resultado.append(carro)
        time.sleep(1)
        linhasF("resultado da pesquisa")
        time.sleep(1)
        if not resultado:
            print("Carro não encontrado!")
        else:
            print("-"*55)
            print(f"{'NOME':<17}    {'PREÇO':<7}    {'ANO':<7}    {'ESTADO':<15}")
            print("-"*55)
            for dado in resultado:
                print(f"{dado[0]:<20} {dado[1]:<10} {dado[2]:<10} {dado[3]:<15}")
                time.sleep(0.5)
            print("-"*55)
    else:
        for carro in carros:
            if carro[3] == pesquisa.strip().lower():
                resultado.append(carro)
        time.sleep(1)
        linhasF("resultado da pesquisa")
        time.sleep(1)
        if not resultado:
            print("Carro não encontrado!")
        else:
            print("-"*55)
            print(f"{'NOME':<17}    {'PREÇO':<7}    {'ANO':<7}    {'ESTADO':<15}")
            print("-"*55)
            for dado in resultado:
                print(f"{dado[0]:<20} {dado[1]:<10} {dado[2]:<10} {dado[3]:<15}")
                time.sleep(0.5)
            print("-"*55)

def cadastrar_carro(nome_arquivo, nome_carro, preco, ano, estado):
    try:
        arquivo = open(nome_arquivo, 'at', encoding='utf-8')
    except:
        print('Houve algum ERRO na abertura do arquivo!')
    else:
        try:
            arquivo.write(f'{nome_carro},{preco},{ano},{estado}\n')
        except:
            print(f"Houve algum ERRO na hora de escrever os dados em '{arquivo}'")
        else:
            print('Novo registro adicionado!')
    finally:
        arquivo.close()
