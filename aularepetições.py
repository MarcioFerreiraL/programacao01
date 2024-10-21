#  1. Façaumprogramaqueexiba os números de 1 a10emordemcrescente.

for i in range(10):
    print(i)


#  2. Crie umprograma que exiba os números de 10 a 1 emordemdecrescente.

for i in reversed(range(10)):
    print('reverso: ',i)

#  3. Elabore umprograma que calcule a soma dos números de 1 a 100.

soma = 0
for i in range(100):
    soma += i
print('soma: ', soma)
    
#  4. Desenvolva um programa que exiba todos os números pares de 1 a 50.

for i in range(0, 51, 2):
    print('pares:',i)

#  5. Façaumprogramaquecalcule o produto dos números de 1 a 5.

lista = [1, 2, 3, 4, 5]
produto = 1
for i in lista:
    produto *= i
print('Produto: ', produto)

#  6. Crie umprograma queexiba a tabuada do 7.

for item in range(1, 11, 1):
    print(f"7 x {item} = {7*item}")

#  7. Elabore umprograma que calcule a média de 5 notas digitadas pelo usuário.

soma = 0
for i in range(1, 6, 1):
    nota = int(input("Digite uma nota: "))
    soma += nota
print(f"A media das notas é {soma/5:.2f}")

#  8. Desenvolva um programa que exiba todos os múltiplos de 3 no intervalo de 1 a 50.

for i in range(3, 51, 3):
    print('multiplo de tres:',i)

#  9. Crie umprograma queleia 10 números do usuário e exiba o maior e o menor valor digitado.

numeros = []
for i in range(0, 10, 1):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
print(max(numeros))
print(min(numeros))

#  10. Faça um programa que exiba os números ímpares de 1 a 100.

for i in range(1, 100, 2):
    print('impares:',i)

#  11. Crie um programa que leia 5 notas de alunos e exiba quantos deles foram aprovados (nota maior
#  ou igual a 7).

alunos = []
for i in range(0, 5, 1):
    alunos.append(int(input(f"Digite uma nota do aluno{i+1}: ")))
for i in range(0, 5, 1):
    if alunos[i] >= 7:
        print(f"O aluno{i+1} foi aprovado!")
    else:
        print(f"O aluno{i+1} foi reprovado!")

#  12. Faça um programa que exiba a soma dos dígitos de um número inteiro fornecido pelo usuário.

numero = int(input("Digite um número inteiro: "))
soma = 0
for digito in str(numero): 
    soma += int(digito)
print(f"A soma dos dígitos de {numero} é: {soma}")

#  13. Elabore um programa que leia um número inteiro e exiba todos os seus divisores.

inteiro = int(input("Digite um numero inteiro: "))
divisor = []
for i in range(inteiro, 0, -1):
    print(i)
    if inteiro%i==0:
        divisor.append(i)
print(f"Os divisores de {inteiro} são {divisor}")

#  14. Desenvolva um programa que calcule a média da altura de 5 pessoas.
alturas = []
for i in range(0, 5):
    altura = float(input("Digite sua altura: "))
    alturas.append(altura)
media = sum(alturas)/len(alturas)
print(f"A media das alturas das pessoas é {media:.2f}")

#  15. Faça um programa que exiba os números de 1 a 100, substituindo os múltiplos de 3 pela palavra
#  "Fizz" e os múltiplos de 5 pela palavra "Buzz". Para os números que são múltiplos de ambos,
#  utilize a palavra "FizzBuzz".

for i in range(0, 101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#  16. Elabore um programa que leia um número inteiro e exiba a soma dos dígitos pares desse número.

numero = int(input("Digite um número inteiro: "))
soma_pares = 0
for digito in str(numero): 
    if int(digito)%2==0:
        soma_pares += int(digito)
print(f"A soma dos dígitos pares é: {soma_pares}")


#  17. Faça um programa que leia um número inteiro e exiba o número invertido. Por exemplo, se o
#  número lido for 123, o programa deve exibir 321

numero = input("Digite um número inteiro: ")
print(numero[::-1])