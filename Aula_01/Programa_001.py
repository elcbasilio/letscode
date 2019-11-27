# comentários #

'''
comentários múltiplos
em várias linhas
utiliza 3 aspas simples para abrir e fechar estes comentários

'''
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
nf=(n1+n2)/2
if nf == 10:
    print('Sua média é',nf,'e você foi Aprovado com Louvor')
elif nf >= 6 and (n1 >= 8 or n2>=8):
    print('Sua média é',nf,'e você foi Aprovado')
elif nf >= 6:
    print('Sua média é',nf,'porém não obteve nenhuma nota acima de 8, logo você foi Reprovado')
else:
    print('Sua média é',nf,'e você foi Reprovado')
