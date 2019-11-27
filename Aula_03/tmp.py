lista=[]
i=1
while i <= 4:
    nota =  float (input ('Digite a nota do',i,'º bimestre:'))
    lista.append(nota)
    i+=1
print ('A média de suas notas bimestrais é',mean(lista))