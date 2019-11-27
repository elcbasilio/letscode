# S01E01 - Episódio 01: Introdução ao Python
# Nosso primeiro programa :)
print('Oi, mundo')

# Primeira modificação do programa, usando variáveis
# mensagem = 'Oi, mundo'
# print(mensagem)

# Principais tipos
texto = 'Sou um texto'
inteiro = 20    # integer
decimal = 3.14  # float
verdade = True  # booleano (True/False)

a = 2
b = 2
# Operadores aritméticos
soma = a + b
subtracao = a - b
multi = a * b
divi = a / b

# Operadores de comparação
maior = a > b
menor = a < b
igual = a == b
maiorOuIgual = a >= b
menorOuIgual = a <= b
diferente = a != b

# Operadores lógicos
operador_e = a == 1 and b == 2
operador_ou = a == 1 or b == 2


# Programa que calcula a média entre duas notas
# O uso do float() é para a conversão de string para número decimal
nota_1 = float(input('Digite a nota 1: '))
nota_2 = float(input('Digite a nota 2: '))
media = (nota_1 + nota_2) / 2
print('a média entre ', nota_1, 'e', nota_2, 'é', media)

tem_alguma_nota_oito = nota_1 >= 8 or nota_2 >= 8
# Se o aluno tem media 10, ele passa com louvor!
# como programar isso?
if media >= 8.0:
    if media == 10:
        print('PASSOU COM LOUVOR!')
    else:
        print('passou direto!')
elif media >= 6.0 and tem_alguma_nota_oito:
    print('passou raspando!')
else:
    print('bombou!')