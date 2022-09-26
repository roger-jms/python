# Programa gerador de senhas aleatórias

import string
import random

l_maiuscula = string.ascii_uppercase
l_minuscula = string.ascii_lowercase
digitos = string.digits
simbolos = string.punctuation

geral = l_maiuscula + l_minuscula + digitos + simbolos
tamanho = 8
senha = ''.join(random.sample(geral, tamanho))
print(f'Sua senha: {senha}')