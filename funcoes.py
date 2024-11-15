# 1. Escreva uma função chamada "soma" que receba dois parâmetros (a e b) e retorne a soma deles.

print("Questão 1")
def soma(n1: int, n2: int):
    resultado = n1 + n2
    return resultado
n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite um numero inteiro: "))
print(soma(n1, n2))

#  2. Crie umafunção chamada "isPar" que receba um número inteiro como parâmetro e retorne "True"
#  se o número for par ou "False" caso contrário.

print("Questão 2")
def isPar(numero:int):
    if numero%2==0:
        return True
    else:
        return False

numero = int(input("Digite um numero:"))
print(isPar(numero))

#  3. Elabore uma função chamada "media" que receba três notas como parâmetros e retorne a média
#  aritmética delas.

print("Questão 3")
def media(nota1:float,nota2:float,nota3:float):
    media = (nota1 + nota2 + nota3)/3
    return media

nota1 = int(input("Digite um numero:"))
nota2 = int(input("Digite um numero:"))
nota3 = int(input("Digite um numero:"))
print(media(nota1, nota2, nota3))

#  4. Elabore uma função chamada "imc" que receba o peso (em kg) e a altura (em metros) de uma
#  pessoa e retorne o índice de massa corporal (IMC) dela.

print("Questão 4")
def imc(peso, altura):
    imc = peso/(altura**2)
    return imc
altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua peso(kg): "))
print(imc(peso, altura))

#  5. Elabore uma função chamada "calcularDesconto" que receba o valor de um produto e o
#  percentual de desconto como parâmetros e retorne o valor com o desconto aplicado.

print("Questão 5")
def calcularDesconto(preco, desconto):
    precoNovo = preco - (preco*(desconto/100))
    return precoNovo
preco = float(input("Digite o preço do produto: "))
desconto = int(input("Digite quantos '%' ele irá receber de desconto: " ))
resultado = calcularDesconto(preco, desconto)
print(f"O preço com desconto é R${resultado}")

#  6. Elabore uma função chamada "calcularImpostoRenda" que receba o salário bruto de uma pessoa
#  comoparâmetro e retorne o valor do imposto de renda a ser pago, considerando as seguintes
#  faixas de renda:
#  a. AtéR$1.903,98: isento
#  b. DeR$1.903,99 até R$ 2.826,65: alíquota de 7,5%
#  c. DeR$2.826,66até R$ 3.751,05: alíquota de 15%
#  d. DeR$3.751,06 até R$ 4.664,68: alíquota de 22,5%
#  e. AcimadeR$4.664,68: alíquota de 27,5%

print("Questão 6")
def calcularImpostoRenda(salarioBruto: float):
    if salarioBruto <=  1903.98:
        return "Isento"
    elif 1903.98 < salarioBruto <= 2826.65:
        return salarioBruto * (7.5/100)
    elif 2826.65 < salarioBruto <= 3751.05:
        return salarioBruto * (15/100)
    elif 3751.05 < salarioBruto <= 4664.68:
        return salarioBruto * (22.5/100)
    elif 4664.68 < salarioBruto:
        return salarioBruto * (27.5/100)

salarioBruto = float(input("Digite o valor em R$ do seu salario bruto: "))
resultado = calcularImpostoRenda(salarioBruto)
if resultado != "Isento":
    print(f"Você tem que pagar R${resultado} do imposto de renda")
else:
    print("Você é isento do imposto de renda!")
    
#  7. Façaumafunção chamada "calcularMediaArredondada" que receba uma lista de números como
#  parâmetro e retorne a média aritmética desses números, arredondada para o inteiro mais
#  próximo.

print("Questão 7")
def calcularMediaArredondada(listaNumeros):
    resultado = sum(listaNumeros/len(listaNumeros))
    return resultado
listaNumeros = []
while True:
    resposta = int(input("Digite um numero inteiro para adicionar a uma lista: (digite 0 se quiser parar) "))
    if resposta == 0:
        break
    else:
        listaNumeros.append(resposta)
resultado = calcularMediaArredondada(listaNumeros)
print(f"A media aritmetica dos numeros que você digitou é {round(resultado)}")

#  8. Desenvolva uma função chamada "contarDigitosParesImpares" que receba um número inteiro
#  comoparâmetro e retorne a quantidade de dígitos pares e a quantidade de dígitos ímpares
#  presentes nesse número.

print("Questão 8")
def contarDigitosParesImpares(numero):
    qnt_digitos_pares = 0
    qnt_digitos_impares = 0
    for i in numero:
        if int(i)%2==0:
            qnt_digitos_pares += 1
        else:
            qnt_digitos_impares += 1
    return qnt_digitos_pares, qnt_digitos_impares
numero = (input("Digite um numero inteiro: "))
resultado = contarDigitosParesImpares(numero)
print(f'A quantidade de digitos pares que você digitou é {resultado[0]} e a quantidade de digitos impares foram {resultado[1]}!') 

#  9. Crie umafunção chamada "calcularMediaAlunos" que receba uma lista de alunos, onde cada aluno
#  é representado por um objeto com os atributos "nome" e "nota". A função deve calcular e
#  retornar a média das notas de todos os alunos.

print("Questão 9")

def calcularMediaAlunos(alunos):
    notas = []
    for nota in str(alunos['nota']):
        print(nota)
        notas.append(int(nota))
    media = sum(notas)/len(notas)
    return media
alunos = {'nome': str, 'nota': int}
while True:
    nome_aluno = input("Digite o nome do aluno: (digite sair se quiser sair) ").lower()
    if nome_aluno == 'sair':
        break
    alunos['nome'] = nome_aluno
    nota_aluno = int(input(f"Digite a nota de {nome_aluno.upper()}: "))
    alunos['nota'] = nota_aluno
print(calcularMediaAlunos(alunos))

#  10. Crie uma função chamada "calcularIdade" que receba o ano de "nascimento" de uma pessoa como
#  parâmetro e retorne a idade atual.

def calcularIdade(nascimento):
    return 2024 - nascimento

#  11. Crie uma função chamada "gerarTabuada" que receba um "número" como parâmetro e exiba a
#  tabuada desse número de 1 a 10 noconsole.

def gerarTabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 12. Escreva uma função chamada "advinheNumero" que gera aleatoriamente um número inteiro entre
#  1 e100. Emseguida, permita que o usuário insira tentativas para adivinhar o número. A função
#  deve dar dicas ao usuário se o número correto é maior ou menor do que a tentativa. Quando o
#  usuário acertar, exiba uma mensagem de parabéns e informe a quantidade de tentativas
#  utilizadas.

import random
def advinheNumero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    while True:
        tentativa = int(input("Adivinhe o número entre 1 e 100: "))
        tentativas += 1
        if tentativa < numero_secreto:
            print("O número correto é maior.")
        elif tentativa > numero_secreto:
            print("O número correto é menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

#  13. Crie uma função chamada "verificarPropriedade" que receba um objeto e uma string como
#  parâmetros, e retorne true se o objeto possuir a propriedade com o nome especificado na string, e
#  false caso contrário.

#  14. Faça uma função chamada "calcularPrecoProduto" que receba o "valor de custo" de um produto, a
#  "margem delucro" desejada (em percentual) e o "valor do frete" como parâmetros. A função deve
#  calcular e retornar o preço de venda do produto, considerando que o preço de venda é igual ao
#  custo acrescido da margem de lucro e do valor do frete.

def calcularPrecoProduto(valor_custo, margem_lucro, valor_frete):
    lucro = valor_custo * (margem_lucro / 100)
    preco_venda = valor_custo + lucro + valor_frete
    return preco_venda

#  15. Escreva uma função que aceite uma string como parâmetro e encontre a palavra mais longa dentro
#  da string. String de exemplo: 'Tutorial de desenvolvimento da web'. Resultado esperado:
#  'Desenvolvimento'.

def encontrarPalavraMaisLonga(texto):
    palavras = texto.split()
    palavra_mais_longa = max(palavras)
    return palavra_mais_longa

#  16. Escreva uma função que pegue uma lista de strings e as imprima, uma por linha, em um quadro
#  retangular. Por exemplo, a lista ["Hello", "World", "in", "a", "frame"] é impressa como:
#  *********
#  * Hello *
#  * World *
#  * inaasfasfasfasf
#  *
#  * a
#  *
#  * frame *
#  *********

def imprimirEmQuadro(lista):
    tamanho_max = max(palavra)
    print('*' * (tamanho_max + 4))
    for palavra in lista:
        print(f"* {palavra(tamanho_max)} *")
    print('*' * (tamanho_max + 4))

#  17. Crie uma função que receba um array de strings e retorne um novo array contendo apenas as
#  strings que têm mais de 5 caracteres.

def filtrarStringsLongas(strings):
    return [s for s in strings if len(s) > 5]

#  18. Crie uma função que recebe um array de objetos com informações sobre livros (título, autor, ano,
#  etc.) e retorne um novo array apenas com os livros escritos por determinado autor.

def filtrarLivrosPorAutor(livros, autor, ano):
    resultado = []
    for livro in livros:
        if livro['autor'] == autor:
            resultado.append(livro)
    return resultado

#  19. Crie uma função que recebe um array de objetos representando pessoas (com nome, idade, etc.) e
#  retorne o nome da pessoa mais velha.

def encontrarPessoaMaisVelha(pessoas):
    pessoa_mais_velha = max(pessoas['idade'])
    return pessoa_mais_velha['nome']

#  20. Escreva uma função que recebe um array de objetos com informações sobre carros (com marca,
#  modelo, ano, etc.) e retorne um novo array apenas com os carros fabricados após um certo ano
#  específico.

def filtrarCarrosPorAno(carros, ano_limite):
    resultado = []
    for carro in carros:
        if carro['ano'] < ano_limite:
            resultado.append(carro['nome'])
    return resultado

#  21. Crie uma função chamada "inverterString" que recebe uma string como argumento e retorna a
#  string invertida. Por exemplo, para a entrada "hello", a função deve retornar "olleh".

def inverterString(texto):
    return texto[::-1]