# 1. Peça a idade do usuário e imprima se ele é maior ou menor de 18 anos;
idade = int (input ('Digite sua idade:'))
if idade < 18:
    print ('Você tem menos de 18 anos')
else:
    print ('Você tem 18 anos ou mais')

# 2. Peça um número e mostre se ele é positivo ou negativo;

numero = float (input ('Digite um número qualquer:'))
if numero  < 0:
    print ('Este número é Negativo')
else:
    print ('Este número é Positivo')

# 3. Dado um número digitado, mostre se ele é Par ou Ímpar

numero = int (input ('Digite um número inteiro:'))
if numero % 2 == 0:
    print ('Este número é Par')
else:
    print ('Este número é Ímpar')

# 4. Peça dois números e mostre o maior deles;

n1 = float (input ('Digite um número qualquer:'))
n2 = float (input ('Digite mais um número qualquer:'))
if n1  < n2:
    print ('O número',n1,'é menor que o número',n2)
elif n1  > n2:
    print ('O número',n1,'é maior que o número',n2)
else:
    print ('Os números digitados são idênticos')

# 5. Faça um programa que leia a validade das informações:
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro;
# O programa deve imprimir uma mensagem de erro para cada informação inválida.

idade = int (input ('Digite sua idade:'))
salario = float (input ('Digite seu salário R$:'))
sexo = input ('Digite seu Sexo (M / F / O):')
if idade  < 0 or idade > 150:
    print ('A idade informada é inválida, digite uma idade entre 0 e 150 anos')
if salario <= 0:
    print ('O salário informado é inválido, digite um valor maior que 0')
if sexo != 'M' and sexo != 'F' and sexo != 'O' and sexo != 'm' and sexo != 'f' and sexo != 'o':
    print ('O sexo informado é inválido, digite M, F ou O')

# 6. Escreva um programa que peça a nota de 3 provas de um aluno, e verifique se ele passou o não de ano:
# Obs: O aluno irá passar de ano se sua média for maior que 6.

n1 = float (input ('Digite sua 1ª Nota:'))
n2 = float (input ('Digite sua 2ª Nota:'))
n3 = float (input ('Digite sua 3ª Nota:'))
nf = (n1+n2+n3)/3
if nf <= 6:
    print ('Sua nota média foi',nf,'e você foi REPROVADO!')
else:
    print ('Sua nota média foi',nf,'e você foi APROVADO!')

# 7. Fazer um programa que mostre uma questão de múltipla escolha com 5 opções (letras a, b, c, d, e e). 
# Sabendo a resposta certa, receber a opção do usuário e informar a letra que o usuário marcou e se a 
# resposta está certa ou errada.

print ('Escolha a alternativa correta')
print ('')
print ('Pergunta: Quem descobriu o Brasil?')
print ('')
print ('a) Vasco da Gama')
print ('b) Jair Bolsonaro')
print ('c) Silvio Santos')
print ('d) Pedro Álvares Cabral')
print ('e) Craque Neto 10')
print ('')
pergunta = (input ('Qual é a resposta correta: '))
if pergunta == 'd' or pergunta == 'D':
    print ('Você selecionou a opção d) Pedro Álvares Cabral. A resposta está correta')
elif pergunta == 'a' or pergunta == 'A':
    print ('Você selecionou a opção a) Vasco da Gama. A resposta está errada')
elif pergunta == 'b' or pergunta == 'B':
    print ('Você selecionou a opção b) Jair Bolsonaro. A resposta está errada')
elif pergunta == 'c' or pergunta == 'C':
    print ('Você selecionou a opção c) Silvio Santos. A resposta está errada')
elif pergunta == 'e' or pergunta == 'E':
    print ('Você selecionou a opção e) Craque Neto 10. A resposta está errada')
else:
    print ('Você selecionou uma opção inválida')

# 8. Vamos fazer um programa para verificar quem é o assassino de um crime.
# Para descobrir a polícia reuniu um dos suspeitos e fez um pequeno questionário com 5 perguntas de sim ou não:
# a. Telefonou para a vítima?
# b. Esteve no local do crime?
# c. Mora perto da vítima?
# d. Devia para a vítima?
# e. Já trabalhou com a vítima?
# Cada resposta sim dá um ponto para o suspeito, a polícia considera que os
# suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices
# e 2 pontos são apenas suspeitos, necessitando outras investigações, valores
# abaixo de 1 são liberados.

print ('Responda S para Sim e N para Não em cada uma das perguntas abaixo')
print ('')
p1 = input ('Telefonou para a vítima?')
p2 = input ('Esteve no local do crime?')
p3 = input ('Mora perto da vítima?')
p4 = input ('Devia para a vítima?')
p5 = input ('Já trabalhou com a vítima?')
if p1 == 's' or p1 == 'S':
    p11 = 1
else:
    p11 = 0
if p2 == 's' or p1 == 'S':
    p22 = 1
else:
    p22 = 0
if p3 == 's' or p1 == 'S':
    p33 = 1
else:
    p33 = 0
if p4 == 's' or p1 == 'S':
    p44 = 1
else:
    p44 = 0
if p5 == 's' or p1 == 'S':
    p55 = 1
else:
    p55 = 0
soma = p11+p22+p33+p44+p55
print ('')
if soma == 5:
    print ('Você é o Assassino')
elif soma >= 3:
    print ('Você é Cúmplice')
elif soma >= 1:
    print ('Você é Suspeito')
else:
    print ('Você está Liberado')

# 9. Um produto vai sofrer aumento de acordo com a tabela 1 abaixo, peça para
# o usuário digitar o valor do produto de acordo com o preço antigo e
# escreva uma das mensagens da tabela 2, de acordo com o preço reajustado:
# Preço antigo Percentual de aumento
# Até R$ 50 5%
# Entre R$ 50 e R$100 10%
# Entre R$100 e R$150 13%
# Acima de R$150 15%
# Preço Novo Mensagem
# Ate R$80 Barato
# Entre R$ 80 e R$115 Razoável
# Entre R$ 115 e R$150 Normal
# Entre R$ 150 e R$170 Caro
# Acima de R$170 Muito caro

print ('Reajuste de Preços')
pa = float (input ('Digit o preço do produto que será reajustado: R$ '))
if pa <= 0:
    print ('Digite um valor maior que ZERO')
    pn=0
elif pa <= 50:
    pn = pa * 1.05
elif pa <= 100:
    pn = pa * 1.1
elif pa <= 150:
    pn = pa * 1.13
else:
    pn = pa * 1.15
if pn <= 0:
    print ('')
elif pn < 80:
    print ('O novo valor do produto é R$',pn,'- Barato')
elif pn < 115:
    print ('O novo valor do produto é R$',pn,'- Razoável')
elif pn < 150:
    print ('O novo valor do produto é R$',pn,'- Normal')
elif pn < 170:
    print ('O novo valor do produto é R$',pn,'- Caro')
else:
    print ('O novo valor do produto é R$',pn,'- Muito Caro')

# Desafio

# 1. Faça um programa que leia 3 números e informe o maior deles;

n1 = float (input ('Digite o 1º Número: '))
n2 = float (input ('Digite o 2º Número: '))
n3 = float (input ('Digite o 3º Número: '))
if n1 >= n2 and n1 >= n3:
    print ('O maior número é',n1)
elif n2 >= n1 and n2 >= n3:
    print ('O maior número é',n2)
elif n3 >= n1 and n3 >= n2:
    print ('O maior número é',n3)

# 2. Agora faça com 4 números;

n1 = float (input ('Digite o 1º Número: '))
n2 = float (input ('Digite o 2º Número: '))
n3 = float (input ('Digite o 3º Número: '))
n4 = float (input ('Digite o 4º Número: '))
if n1 >= n2 and n1 >= n3 and n1 >= n4:
    print ('O maior número é',n1)
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    print ('O maior número é',n2)
elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    print ('O maior número é',n3)
elif n4 >= n1 and n4 >= n2 and n4 >= n3:
    print ('O maior número é',n4)

'''
3. Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um
questionário de sintomas, tendo as perguntas abaixo, faça um programa
que faça o diagnóstico deste hospital:
a. Sente dor no corpo?
b. Você tem febre?
c. Você tem tosse?
d. Está com congestão nasal?
e. Tem manchas pelo corpo?
Para o diagnóstico ele tem a seguinte tabela:
A B C D E Resultado
Sim Sim Não Não Sim Dengue
Sim Sim Sim Sim Não gripe
Não Sim Sim Sim Não gripe
Sim Não Sim Sim Não Gripe
Sim Não Não Não Não Sem Doenças
Não Não Não Não Não Sem Doenças
'''
print ('Diagnóstico de gripe ou dengue')
print ('')
print ('Digite S para "Sim" ou N para "Não"')
print ('')
p1 = (input ('Sente dor no corpo? '))
p2 = (input ('Você tem febre? '))
p3 = (input ('Você tem tosse? '))
p4 = (input ('Está com congestão nasal? '))
p5 = (input ('Tem manchas pelo corpo? '))
if (p1.upper()!='S' and p1.upper()!='N') and (p2.upper()!='S' and p2.upper()!='N') and (p3.upper()!='S' and p3.upper()!='N') and (p4.upper()!='S' and p4.upper()!='N') and (p5.upper()!='S' and p5.upper()!='N'):
    print ('Você digitou uma ou mais opções incorretas')
elif p1.upper()=='S' and p2.upper()=='S' and p3.upper()=='N' and p4.upper()=='N' and p5.upper()=='S':
    print ('Diagnóstico - Dengue')
elif p1.upper()=='S' and p2.upper()=='S' and p3.upper()=='S' and p4.upper()=='S' and p5.upper()=='N':
    print ('Diagnóstico - Gripe')
elif p1.upper()=='N' and p2.upper()=='S' and p3.upper()=='S' and p4.upper()=='S' and p5.upper()=='N':
    print ('Diagnóstico - Gripe')
elif p1.upper()=='S' and p2.upper()=='N' and p3.upper()=='S' and p4.upper()=='S' and p5.upper()=='N':
    print ('Diagnóstico - Gripe')
elif p1.upper()=='S' and p2.upper()=='N' and p3.upper()=='N' and p4.upper()=='N' and p5.upper()=='N':
    print ('Diagnóstico - Sem Doenças')
elif p1.upper()=='N' and p2.upper()=='N' and p3.upper()=='N' and p4.upper()=='N' and p5.upper()=='N':
    print ('Diagnóstico - Sem Doenças')
else:
    print ('Diagnóstico - Diagnóstico não está especificado')
