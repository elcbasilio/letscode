# COMANDO WHILE 
print ('Seja bem-vindo ao Pyrque')
# looping infinito (CUIDADO)
while True:
    local = input ('Digite o local que deseja ir: ')
    if local != 'Embora':
        print ('Uhu!!!!')
    else:
        print ('Volte logo!')
        break

# COMANDO WHILE - OUTRA MANEIRA
print ('Seja bem-vindo ao Pyrque')
# looping infinito (CUIDADO)
while True:
    print ('1 - Montanha Russa')
    print ('2 - Barco Viking')
    print ('3 - Carrinho bate-bate')
    print ('0 - Embora')
    local = int (input ('Digite o local que deseja ir: '))
    if 1<= local <= 3:
        print ('Uhu!!!!')
    elif local != 0:
        print ('Digite um número válido')
    else:
        print ('Volte logo!')
        break


# COMANDO WHILE - MELHOR RESOLUÇÃO
print ('Seja bem-vindo ao Pyrque')
# looping infinito (CUIDADO)
while True:
    print ('1 - Montanha Russa')
    print ('2 - Barco Viking')
    print ('3 - Carrinho bate-bate')
    print ('0 - Embora')
    local = (input ('Digite o local que deseja ir: '))
    if local == '1' or local == '2' or local == '3':
        print ('Uhu!!!!')
    elif local != '0':
        print ('Digite um número válido')
    else:
        print ('Volte logo!')
        break

# Imprimir 1 2 4 8 16 32 64 128 256 512

numero=1
while numero <= 512:
    print (numero)
    numero = numero * 2


# Imprimir N VALORES = 1 2 4 8 16 32 64 128 256 512....

qtde = int (input ('Digite a quantidade de valores que deseja imprimir: '))
numero=1
inicio = 1
while inicio <= qtde:
    print (numero)
    numero *= 2
    inicio += 1