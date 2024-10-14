# 1. Escreva um programa que leia um número inteiro e verifique se ele é positivo, negativo ou igual a
# zero

numero = int(
    input("Digite um numero para verificar se ele é positivo, negativo ou neutro: "))
if numero > 0:
    print(f"O numero {numero} é positivo!")
elif numero < 0:
    print(f"O numero {numero} é negativo!")
elif numero == 0:
    print(f"O numero {numero} é igual a zero!")
else:
    print("Erro!, digite um numero válido!")

# 2. Crie um programa que receba a idade de uma pessoa e exiba se ela é maior de idade ou menor de
# idade.

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print(f"Você é maior de idade!")
elif idade < 18:
    print(f"Você é menor de idade!")
else:
    print("Erro!, digite uma idade válida!")

# 3. Desenvolva um programa que leia dois números inteiros e mostre qual deles é o maior, ou se são
# iguais.

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}")
elif numero1 < numero2:
    print(f"{numero2} é maior que {numero1}")
elif numero1 == numero2:
    print(f"{numero2} e {numero1} são iguais!")
else:
    print("Erro!, digite um numero válido!")

# 4. Faça um programa que verifique se um número é par ou ímpar.

numero = int(input("Digite um numero: "))
if numero % 2 == 0:
    print(f"{numero} é par!")
else:
    print(f"{numero} é impar!")

# 5. Elabore um programa que leia três notas de um aluno e calcule a média. Em seguida, exiba se o
# aluno está aprovado (média maior ou igual a 7) ou reprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1+nota2+nota3)/3
if media >= 7:
    print(f"A media das notas é {media:.2f} e o aluno está aprovado!")
elif media < 7:
    print(f"A media das notas é {media:.2f} e o aluno está reprovado!")
else:
    print("Erro!, digite notas válido!")

# 6. Crie um programa que receba o nome de duas pessoas e exiba qual delas possui o maior número
# de caracteres em seu nome.

nome1 = (input("Digite o nome de uma pessoa: "))
nome2 = (input("Digite o nome de outra pessoa: "))
if len(nome1) > len(nome2):
    print(f"{nome1} tem mais caracteres que {nome2}")
elif len(nome1) < len(nome2):
    print(f"{nome2} tem mais caracteres que {nome1}")
elif len(nome1) == len(nome2):
    print(f"{nome2} tem a mesma quantidade de caracteres {nome1}")

# 7. Desenvolva um programa que leia um caractere e verifique se ele é uma vogal ou uma consoante.

umCaractere = (input("Digite apenas um caractere ")).lower()
if umCaractere[0] == "a" or umCaractere[0] == "e" or umCaractere[0] == "i" or umCaractere[0] == "o" or umCaractere[0] == "u":
    print(f"'{umCaractere}' é uma vogal!")
else:
    print(f"'{umCaractere}' é uma consoante!")

# 8. Faça um programa que receba três números e os imprima em ordem crescente.

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
numero3 = int(input("Digite um numero: "))
if numero1 >= numero2 >= numero3:
    print(numero1, ' ', numero2, ' ', numero3)
elif numero1 >= numero3 >= numero2:
    print(numero1, ' ', numero3, ' ', numero2)
elif numero3 >= numero2 >= numero1:
    print(numero3, ' ', numero2, ' ', numero1)
elif numero3 >= numero1 >= numero2:
    print(numero3, ' ', numero1, ' ', numero2)
elif numero2 >= numero3 >= numero1:
    print(numero2, ' ', numero3, ' ', numero1)
elif numero2 >= numero1 >= numero3:
    print(numero2, ' ', numero1, ' ', numero3)

# 9. Elabore um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa, dado o peso e
# a altura. Em seguida, exiba se a pessoa está abaixo do peso, com peso normal, com sobrepeso,
# obesa ou muito obesa.

altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua peso(kg): "))
imc = peso/(altura*2)
if imc < 18.5:
    print("Abaixo do peso")
elif 24.9 > imc > 18.6:
    print("Peso normal")
elif 29.9 > imc > 25:
    print("Sobrepeso")
elif 34.9 > imc > 30:
    print("Obesa")
elif imc > 35:
    print("Muito obesa")

# 10. Escreva um programa que receba um número de mês (1 a 12) e exiba o nome do mês
# correspondente.

mes = int(input("Digite o numero de algum mes(1 à 12): "))
if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Digite um mes valido!")

# 11. Desenvolva um programa que leia o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.500,00, o aumento deve ser de 10%. Caso contrário, o aumento é de
# 15%.

salario = float(input("Digite o seu salario: "))
if salario > 1500:
    aumento = salario * 0.1
    salario = salario + aumento
elif salario <= 1500:
    aumento = salario * 0.15
    salario = salario + aumento
print(f"O seu salario recebeu um aumento de R${aumento:.2f} e agora o seu salario é R${salario:.2f}")

# 12. Receba um número inteiro do usuário e verifique se ele é divisível por 3 e por 5 ao mesmo tempo,
# exibindo uma mensagem apropriada.

numero = int(input("Digite um numero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f"O numero {numero} é divisivel por 3 e por 5!")
else:
    print(f"O numero {numero} não é divisivel por 3 e por 5!")

# 13. Peça ao usuário que insira o dia da semana (por extenso) e, em seguida, exiba uma mensagem
# informando se é um dia útil ou um fim de semana.

diaSemana = (
    input("Digite um dia na semana por extenso(Ex: Segunda): ")).lower()
if diaSemana == "segunda" or diaSemana == "terça" or diaSemana == "quarta" or diaSemana == "quinta" or diaSemana == "sexta":
    print(f"{diaSemana} é um dia útil!")
elif diaSemana == "domingo" or diaSemana == "sabado":
    print(f"{diaSemana} não é um dia útil!")
else:
    print("Digite um dia da semana válido!")

# 14. Elabore um programa que leia um número inteiro de 1 a 5 e exiba a mensagem "Muito bom",
# "Bom", "Regular", "Insuficiente" ou "Muito insuficiente", de acordo com o valor lido.

avaliacao = int(input("Digite um numero de 1 à 5: "))
if avaliacao == 5:
    print("Muito bom")
elif avaliacao == 4:
    print("Bom")
elif avaliacao == 3:
    print("Regular")
elif avaliacao == 2:
    print("Insuficiente")
elif avaliacao == 1:
    print("Muito insuficiente")
else:
    print("Digite um numero de 1 à 5!")

# 15. Peça ao usuário que digite um número entre 1 e 7 e exiba o dia da semana correspondente (1 -
# Domingo, 2 - Segunda-feira, etc.).

diaSemana = int(input("Digite um numero de algum dia na semana(1 à 7): "))
if diaSemana == 1:
    print("Domingo")
elif diaSemana == 2:
    print("Segunda-feira")
elif diaSemana == 3:
    print("Terça-feira")
elif diaSemana == 4:
    print("Quarta-feira")
elif diaSemana == 5:
    print("Quinta-feira")
elif diaSemana == 6:
    print("Sexta-feira")
elif diaSemana == 7:
    print("Sabado")
else:
    print("Digite um numero de 1 à 7!")

# 16. Receba um número decimal do usuário e arredonde-o para o inteiro mais próximo usando a
# estrutura de controle try/except para tratar possíveis exceções.

try:
    numero = float(input("Digite um numero decimal: "))
    print((round(numero)))
except:
    print("Digite um numero válido")

# 17. Peça ao usuário que insira a sua idade e verifique se ele é um bebê (0 a 1 ano), criança (1 a 12
# anos), adolescente (13 a 18 anos) ou adulto (mais de 18 anos).

idade = int(input("Digite sua idade: "))
if 0 < idade < 1:
    print("Bebê")
elif 1 < idade < 12:
    print("Criança")
elif 13 < idade < 18:
    print("adolescente")
elif idade > 18:
    print("adulto")
else:
    print("Digite uma idade válida!")

# 18. Solicite ao usuário dois números inteiros e, com base na operação escolhida pelo usuário (1 - para
# soma, 2 - para subtração, 3 - para multiplicação ou 4 - para divisão), exiba o resultado da operação.

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
operacao = int(input("Digite a operação que você deseja fazer com os dois numero(1 - para soma, 2 - para subtração, 3 - para multiplicação ou 4 - para divisão: "))
if operacao == 1:
    resultado = numero1 + numero2
    print(f"o resultado de {numero1} + {numero2} = {resultado}")
elif operacao == 2:
    resultado = numero1 - numero2
    print(f"o resultado de {numero1} - {numero2} = {resultado}")
elif operacao == 3:
    resultado = numero1 * numero2
    print(f"o resultado de {numero1} * {numero2} = {resultado}")
elif operacao == 4:
    resultado = numero1 / numero2
    print(f"o resultado de {numero1} / {numero2} = {resultado}")
else:
    print("Error")

# 19. Desenvolva um programa que leia o nome e a idade de uma pessoa. Utilize o bloco try/except para
# garantir que a idade digitada seja um valor inteiro válido.

nome = input("Digite o seu nome: ")
try:
    idade = int(input("Digite sua idade: "))
except:
    print("Digite uma idade válida!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")

# 20. Crie um programa que leia um valor em metros e o converta para centímetros, milímetros e
# quilômetros. Utilize o bloco try/except para lidar com possíveis exceções que possam vir a
# acontecer durante os cálculos.

try:
    metros = float(input("Digite uma quantidade de metro: "))
    centimetros = metros * 100
    milimetro = metros * 1000
    quilometro = metros * 0.001
    print(f"{metros}m = {centimetros}cm = {milimetro}mm = {quilometro}km.")
except:
    print("Digite um numero válido!")
