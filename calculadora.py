# Calculadora em Python

print("Calculadora em Python - Roger")
print("Selecione a Operação Desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Digite sua opção (1/2/3/4): "))

x = int(input("Digite primeiro número: "))
y = int(input("Digite segundo número: "))

if operacao == 1:
    soma = x + y
    print(f'A soma de {x} com {y} é {soma}')
elif operacao == 2:
    subtracao = x - y
    print(f'A subtração de {x} por {y} é {subtracao}')
elif operacao == 3:
    multiplicacao = x * y
    print(f'A multiplicação de {x} por {y} é {multiplicacao}')
elif operacao == 4:
    divisao = x / y
    print(f'A divisão de {x} por {y} é {divisao}')
else:
    print("Sua opção é inválida")
