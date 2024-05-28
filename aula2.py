import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num_1 = int(input ("Digite um número: "))
# num_2 = int(input ("Digite um número: "))
# sum = num_1 + num_2
# print(f"A soma dos valores é {sum}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# num_1 = int(input ("Digite um número: "))
# div = num_1 % 5
# print(f"O resto da divisão é {div}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num_1 = float(input ("Digite um número: "))
# num_2 = float(input ("Digite um número: "))
# sum = num_1 + num_2
# print (f"{sum:.1f}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite a área do circulo: "))
# area = math.pi * raio **2
# print (f"{area:.2f}")
# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = str(input("Digite uma data no formato dd/mm/aaaa: "))
# data_separada = data.split("/")
# print (f"Dia: {data_separada[0]}")
# print (f"Mês: {data_separada[1]}")
# print (f"Ano: {data_separada[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# nome1 = str(input("Digite alguma coisa: "))
# nome2 = str(input("Digite alguma coisa: "))
# concat = print(nome1 +" "+ nome2)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura

# try:

#     temperatura = (int(input("Digite um valor de temperatura em Celsius: ")))
#     fahrenheit = ((temperatura*9/5) + 32)
#     print(f"{fahrenheit:.2f}º fahrenheit")

# except ValueError:
#     print("Favor digite um valor inteiro")
# 22: Verificador de Palíndromo

entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")
# 23: Calculadora Simples
    try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")
# 24: Classificador de Números
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
# 25: Conversão de Tipo com Validação
    entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
