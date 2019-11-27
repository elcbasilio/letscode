# Peça ao usuário um número, e imprima todos os números de um ao
# número dado: Exemplo: digite: 5 imprime: 1 2 3 4 5

numero = int (input('Digite um número: '))
i=1
while i <= numero:
    print (i) 
    i+=1


# 2. Peça ao usuário para digitar um número n e some todos os números de 1 a n.

numero = int (input('Digite um número maior que zero: '))
n=1
soma=0
while n <= numero:
    soma=n+soma
    n+=1
print(soma)


# 3. Peça ao usuário para digitar um número e imprima o fatorial de n.

numero = int (input('Digite um número maior que zero: '))
soma = 1
i = 1
while numero >= 1: 
    soma = soma * i
    numero -= 1
    i += 1
print (soma)


# 4. Faça um programa que imprima a tabuada de 9 (de 9*1 a 9*10) usando loops.

numero = int (input('Digite um número maior que zero: '))
i=1
while i <= 10:
    print(numero, '*', i, '=',numero*i)
    i+=1


# 5. Dado um número, imprima na tela todos os seus divisores.

numero = int (input('Digite um número maior que zero: '))
i=1
while i <= numero:
    if numero % i == 0:
        print(i)
        i+=1
    else:
        i+=1

# 6. Faça um programa, usando loops, que peça para um usuário digitar um número e que só finaliza 
# quando o usuário digitar 0. Ao final imprima a soma de todos os números digitados

numero = 1
soma=0
while numero != 0:
    numero = int (input('Digite um número: '))
    soma=soma+numero
print (soma)


# 7. Faça um programa que peça para o usuário digitar a idade, o salário e o
# sexo até que as entradas digitadas sejam válidas

sexo = input ('Digite o sexo (M ou F): ')
while sexo.upper() != 'F' and sexo.upper() != 'M':
    print ('Digite corretamente o sexo')
    sexo = input ('Digite o sexo (M ou F): ')
idade = int (input ('Digite sua idade: '))
while idade < 0 or idade > 120:
    print ('Digite corretamente a idade')
    idade = int (input ('Digite sua idade: '))
salario = float (input ('Digite seu salário: R$ '))
while salario < 0:
    print ('Digite corretamente o salário')
    salario = float (input ('Digite seu salário: '))


# Desafio
# 1. Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
# Dica: use três variáveis: um contador, que começa em zero; uma variável
# para a soma de todos os termos, que também começa em zero; uma
# variável para cada termo, que começa em 1 e a cada loop é dividida por 2.
# A repetição da soma de mil termos pode ser feita com a função while contador < 1000.

num_termos = int (input ('Digite a quantidade de termos: '))
serie = 1
contador = 1
soma = 0
while contador <= num_termos:
    soma = soma + 1 / serie
    serie *= 2
    contador += 1
print (soma)


# 2. Super Desafio! - Calcule a soma de mil termos dos inversos dos fatoriais:
# 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
# Dica: assim como no exercício anterior use três variáveis: um contador;
# uma variável para a soma; e uma variável para os termos. Lembre-se de
# que 4! = 4*3*2*1 que também é igual a 4*3!.

print ('Calcule a soma de N termos dos inversos dos fatoriais')
print ('')
numero = int (input('Digite um número maior que zero: '))
fatorial = 1
incremento_fat = 1
fat_inv = 0
while numero >= 1: 
    fatorial = fatorial * incremento_fat
    numero -= 1
    incremento_fat += 1
    fat_inv = (1 / fatorial) + fat_inv
print (fat_inv)