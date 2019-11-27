# 1. Faça um Programa que mostre a mensagem "Alô mundo" na tela.
mensagem = 'Alô, Mundo'
print (mensagem)
#
# 2. Faça um Programa que peça um número e mostre a mensagem "O número informado foi [número]".
numero = input ('Digite um número:')
print ('O número informado foi',numero)

# 3. Faça um Programa que peça dois números e imprima a soma.
n1 = float(input ('Digite o 1º número:'))
n2 = float(input ('Digite o 2º número:'))
print ('A soma de',n1,'e',n2,'é',(n1+n2))

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = float (input('Digite a nota do 1º Bimestre:'))
n2 = float (input('Digite a nota do 2º Bimestre:'))
n3 = float (input('Digite a nota do 3º Bimestre:'))
n4 = float (input('Digite a nota do 4º Bimestre:'))
print ('A média de suas 4 notas bimestrais é',((n1+n2+n3+n4)/4))

# 5. Faça um Programa que converta metros para centímetros.
medida = float (input('Digite o tamanho em metros:'))
print ('O tamanho',medida,'metro(s) é igual a',(medida * 100),'centímetros')

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# Obs: Fórmula da área de um círculo, A = 3.14*r²
r = float (input('Digite o raio do círculo (em centímetros):'))
area = 3.14*r**2
print ('O tamanho da área deste círculo é',area,'centímetros')

# 7. Faça um Programa que pede para o usuário digitar o tamanho do lado de um quadrado, 
# em seguida calcule a área.
lado = float (input('Digite o tamanho do lado de um quadrado (em centímetros):'))
area = lado**2
print ('O tamanho da área deste quadrado é',area,'centímetros')

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
hora = float (input('Digite o valor que você recebe por hora:'))
qtde = int (input('Digite a quantidade de horas trabalhadas no mês:'))
valor = hora * qtde
print ('O seu salário neste mês será R$',hora,'/ hora *',qtde,'horas trabalhadas = R$',valor)

# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em 
# graus Celsius. C = (5 * (F-32) / 9).

F = float (input('Digite o valor da temperatura em Fahrenheit:'))
C = ((F-32) * 5 / 9)
print ('A temperatura',F,'graus Fahrenheit é a mesma coisa que',C,'graus Celsius')

# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = float (input('Digite o valor da temperatura em Celsius:'))
F = (C * 9 / 5) + 32 
print ('A temperatura',C,'graus Celsius é a mesma coisa que',F,'graus Fahrenheit')

# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

n1 = int (input('Digite um número inteiro:'))
n2 = int (input('Digite outro número inteiro:'))
n3 = float (input('Agora digite um número real:'))

# a) o produto do dobro do primeiro com metade do segundo.

resp_a = (n1 * 2) * (n2 / 2)
print ('O produto do dobro do primeiro com metade do segundo é',resp_a)

# b) a soma do triplo do primeiro com o terceiro.

resp_b = (n1 * 3) + (n3)
print ('A soma do triplo do primeiro com o terceiro é',resp_b)

# c) o terceiro elevado ao cubo.

resp_c = (n3 ** 3)
print ('O terceiro elevado ao cubo é',resp_c)

# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: Peso Ideal = (72.7*altura) – 58

altura = int (input('Digite sua altura em centímetros:'))
peso = ((72.7 * (altura/100)) - 58)
print ('Seu peso ideal é',peso)

# 13. Faça um programa que peça o peso e altura e calcule o IMC da pessoa;

altura = int (input('Digite sua altura em centímetros:'))
peso = float (input('Digite seu peso em quilos:'))
imc = (peso / ((altura/100)**2))
if imc < 18.5:
    print ('Seu Índice de Massa Corpórea é',imc,'e você está ABAIXO DO PESO')
elif imc < 25:
    print ('Seu Índice de Massa Corpórea é',imc,'e você está com o PESO NORMAL')
elif imc < 30:
    print ('Seu Índice de Massa Corpórea é',imc,'e você está com SOBREPESO')
elif imc < 35:
    print ('Seu Índice de Massa Corpórea é',imc,'e você está com OBESIDADE GRAU 1')
elif imc < 40:
    print ('Seu Índice de Massa Corpórea é',imc,'e você está com OBESIDADE GRAU 2')
else:
    print ('Seu Índice de Massa Corpórea é',imc,'e você está com OBESIDADE GRAU 3')

# Desafio
# 1. Peça para o usuário digitar uma velocidade inicial, uma posição inicial e um instante de tempo e 
# imprima a posição de um projétil nesse instante de tempo;
# Dica: use a fórmula matemática y(t) = y(0) + V(0).t + ½(g.t²)

print ('Calculando a Função Horária de Movimento Vertical')
print ('')
v0 = int (input('Digite a Velocidade Inicial (m/s):'))
y0 = float (input('Digite a Posição Inicial:'))
t = float (input('Digite o Instante de Tempo:'))
g = 9.80665
mruv = y0 + v0 * t + (0.5 * g * t**2)
print ('Função Horária de Movimento Vertical é',mruv)
