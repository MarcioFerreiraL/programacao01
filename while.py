# 1. Enumere as diferenças entre os comandos "for" e "while".

print("O for é usado para percorrer lista ou executar o algoritmo quantas vezes o programador desejar")
print("O while é usado quando o programador quer que uma condição seja satisfeita.")

# 2. Descreva em quais circunstâncias os comandos "for" e "while" devem ser empregados.

print("O for é usado para percorrer lista ou executar o algoritmo quantas vezes o programador desejar")
print("O while é usado quando o programador quer que uma condição seja satisfeita.")

# 3. Escreva um programa que exiba os números de 1 a 10 em ordem crescente utilizando o while.

contador = 0
while contador < 10:
    print(contador)
    contador += 1

# 4. Crie um programa que exiba os números de 10 a 1 em ordem decrescente utilizando o while.

contador = 10
while contador > 1:
    contador -= 1
    print(contador)

# 5. Elabore um programa que calcule a soma dos números de 1 a 100 utilizando o while.

contador = 0
soma = 0
while contador < 100:
    contador += 1
    soma += contador
print(soma)

# 6. Faça um programa que calcule o produto dos números de 1 a 5 utilizando o while.

contador = 0
produto = 1
while contador < 5:
    contador += 1
    produto *= contador
    print(produto)

# 7. Crie um programa que exiba a tabuada do 9 utilizando o while.

contador = 0
while contador < 10:
    contador += 1
    print(f"9 x {contador} = {9*contador}")

# 8. Crie um programa que leia uma sequência de números inteiros do usuário e exiba o maior e o
# menor valor digitado. O programa deve parar de ler quando o usuário digitar o número 0
# utilizando o while.

resposta = str
numeros = []
while True:
    resposta = int(input("Digite um número inteiro: (digite 0 se quiser parar): "))
    if resposta != 0:
        numeros.append(resposta)
    else:
        break
print(f"O maior numero digitado é {max(numeros)} e o menor numero digitado é {min(numeros)}")

# 9. Crie um programa que leia uma sequência de números inteiros do usuário e exiba a média dos
# números digitados. O programa deve parar de ler quando o usuário digitar o número -1 utilizando
# o while.

resposta = str
numeros = []
while True:
    resposta = int(input("Digite um número inteiro: (digite -1 se quiser parar): "))
    if resposta != -1:
        numeros.append(resposta)
    else:
        break
print(f"A media dos numeros digitados é {sum(numeros)/len(numeros):.2f}")

# 10. Faça um programa que leia um número inteiro e exiba a soma dos seus dígitos elevados ao cubo
# utilizando o while.

inteiro = input("Digite um numero inteiro: ")
soma = 0
for i in inteiro:
    soma += int(i) ** 3
print(soma) 

# 11. Faça um programa que exiba os números ímpares de 1 a 100 utilizando o while.

contador = 1
while contador < 100:
    contador += 1
    if contador%2!=0:
        print(contador)

# 12. Desenvolva um programa que exiba todos os múltiplos de 3 no intervalo de 1 a 50 utilizando o
# while.

contador = 0
while contador < 50:
    contador += 1
    if contador%3==0:
        print(contador)

# 13. Crie um programa que leia 5 notas de alunos e exiba quantos deles foram aprovados (nota maior
# ou igual a 7) utilizando o while.

alunos = 0
aprovados = 0
while alunos < 5:
    alunos += 1
    nota = float(input(f"Digite A nota do aluno{alunos}: "))
    if nota >= 7:
        aprovados += 1
print(f"Foram aprovados {aprovados} alunos")

# 14. Elabore um programa que leia uma sequência de números inteiros do usuário e determine
# quantos números pares foram digitados antes do primeiro número ímpar. O programa deve parar
# de ler quando o usuário digitar o número 0 utilizando o while.

contador = 0
numeros = []
while True:
    resposta = int(input("Digite um número inteiro: (digite 0 se quiser parar): "))
    if resposta != 0:
        numeros.append(resposta)
    else:
        break
for i in numeros:
    if i%2!=0:
        contador += 1
    else:
        break
print(f"Foram digitados {contador} numeros antes do primeiro impar digitado")

# 15. Crie um programa que leia uma sequência de números inteiros do usuário e exiba quantos
# números pares e quantos números ímpares foram digitados. O programa deve parar de ler quando
# o usuário digitar o número 0 utilizando o while.

resposta = str
numerosPares = []
numerosImpares= []
while True:
    resposta = int(input("Digite um número inteiro: (digite 0 se quiser parar): "))
    if resposta != 0:
        if resposta%2==0:
            numerosPares.append(resposta)
        else:
            numerosImpares.append(resposta)
    else:
        break
print(f"Numeros pares digitados {numerosPares}")
print(f"Numeros impares digitados {numerosImpares}")

# 16. Faça um programa que leia uma sequência de números inteiros do usuário e exiba quantos
# números são divisíveis por 2, quantos são divisíveis por 3 e quantos são divisíveis por 5. O
# programa deve parar de ler quando o usuário digitar o número 0 utilizando o while.

resposta = str
divisiveis2 = []
divisiveis3 = []
divisiveis5 = []
while True:
    resposta = int(input("Digite um número inteiro: (digite 0 se quiser parar): "))
    if resposta != 0:
        if resposta%3==0:
            divisiveis3.append(resposta)
        if resposta%2==0:
            divisiveis2.append(resposta)
        if resposta%5==0:
            divisiveis5.append(resposta)
    else:
        break
print(f"Numero divisiveis por 2 {len(divisiveis2)}")
print(f"Numero divisiveis por 3 {len(divisiveis3)}")
print(f"Numero divisiveis por 5 {len(divisiveis5)}")

# 17. Desenvolva um programa que leia uma sequência de números inteiros do usuário e exiba a média
# dos números divisíveis por 3. O programa deve parar de ler quando o usuário digitar o número 0
# utilizando o while.

resposta = str
divisiveis3 = []
while True:
    resposta = int(input("Digite um número inteiro: (digite 0 se quiser parar): "))
    if resposta != 0:
        if resposta%3==0:
            divisiveis3.append(resposta)
    else:
        break
print(f"A media dos numeros divididos por 3 é {sum(divisiveis3)/len(divisiveis3)}")

# 18. Faça um programa que leia uma sequência de números inteiros do usuário e exiba quantos
# números possuem mais de três dígitos. O programa deve parar de ler quando o usuário digitar o
# número 0 utilizando o while.

resposta = str
numeros = []
while resposta != 0:
    resposta = int(input("Digite um número inteiro: (digite 0 se quiser parar): "))
    if resposta != 0:
        if resposta > 999:
            numeros.append(resposta)
    else:
        break
print(f"Você digitou {len(numeros)} numeros com mais de 3 digitos")

# 19. Desenvolva um programa que leia uma sequência de números inteiros do usuário e exiba a média
# dos números que estão entre 50 e 100. O programa deve parar de ler quando o usuário digitar o
# número 0 utilizando o while.

resposta = str
numeros = []
while resposta != 0:
    resposta = int(input("Digite números inteiros separados por um espaço: (digite 0 se quiser parar): "))
    if int(resposta) != 0:
        if 50 <= resposta <= 100:
            numeros.append(resposta)
    else:
        break
print(f"A media dos numeros digitados é {sum(numeros)/len(numeros)}")


# 20. Elabore um programa que leia uma sequência de números inteiros do usuário e exiba o menor
# valor digitado que seja positivo e ímpar. O programa deve parar de ler quando o usuário digitar o
# número 0 utilizando o while.

resposta = str
while resposta != 0:
    resposta = input("Digite um número inteiro: (digite 0 se quiser parar)")
    if int(resposta) != 0:
        menor = resposta+1
        impares = []
        for numero in str(resposta):
            if int(numero)%2!=0:
                impares.append(int(numero))
        for numero in impares:
            if menor > numero:
                menor = numero
        print(menor)
    else:
        print("Tchau :)")


# 21. Faça um programa que leia uma sequência de números inteiros do usuário e exiba quantos
# números são pares e quantos números são ímpares entre o primeiro e o último número digitado.
# O programa deve parar de ler quando o usuário digitar o número 0 utilizando o while.

resposta = str
while resposta != 0:
    resposta = int(
        input("Digite um número inteiro: (digite 0 se quiser parar)"))
    if int(resposta) != 0:
        pares = []
        impares = []
        for numero in str(resposta):
            if int(numero) % 2 == 0:
                pares.append(int(numero))
            else:
                impares.append(int(numero))
        print(f"O numero que voce digitou é {resposta}")
        print(f"Os numeros pares desse numero é {pares} e a quantidade de numeros pares é {len(pares)}")
        print(f"Os numeros impares desse numero é {impares} e a quantidade de numeros impares é {len(impares)}")
    else:
        print("Tchau :)")
