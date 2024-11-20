import os
from funcoes import defs
while True:
    defs.linhasF('Menu Principal')
    defs.linhas()
    print('2 - Pesquisar carros')
    print('1 - Cadastrar novo carro')
    print('0 - Sair do sistema')
    defs.linhas()
    opcao = int(input('Sua opção: '))
    defs.linhas()
    if opcao == 0:
        os.system("cls")
        print("Até breve :)")
        break
    elif opcao == 1:
        os.system("cls")
        print("Digite o nome do carro:")
        nome_carro = input()
        print("Digite o preço(R$) do carro:")
        preco = input()
        print("Digite o ano do carro:")
        ano = input()
        print("Digite o estado do carro: (por exemplo: 'novo', 'seminovo', 'conservado', 'mal estado')")
        estado = input()
        defs.cadastrar_carro('estoque_carros', nome_carro, preco, ano, estado)
    elif opcao == 2:
        os.system("cls")
        defs.buscarCarros('estoque_carros')
    else:
        print('Digite um numero válido!')
