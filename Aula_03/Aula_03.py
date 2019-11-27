# digite notas até digitar compute e depois faz a média 

nota = '0'
soma = 0
incremento = 0
while nota != 'compute':
    nota = input ('Digite uma nota de 0 a 10: ')
    if nota == 'compute':
        print (' ')
    else:
        soma += float (nota)
        incremento += 1
print ('A média será',soma, '/', incremento,'=',soma / incremento)

# mesmo exercicio utilizando listas para armazenar as notas

notas = []
while True:
    nota = input ('Digite uma nota (ou digite "compute" para encerrar): ')
    if nota == 'compute':
        break
    valor = float (nota)
    notas.append (valor)
print (sum(notas) / len (notas))

