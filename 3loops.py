#1
'''for i in range (0,11): 
    print(i)'''

#2
'''for n in range (11,0): 
    print(n)'''
#3 
'''for t in range (0,11,2): 
    print(t)'''

#4
'''num = int (input('Digite um numero: '))
for i in range (0,11):
    print (num * i)'''
#5 
'''nome = 0
lista = []
while nome != 'parar':
    nome = (input('Digite um nome: '))
    lista.append(nome)
for i in lista:
    print(f'Nomes digitados: {i}')
'''
#6
'''soma = 0
num = 0 
while num != -1 :
    num = float(input('Digite um numero: '))
    soma = soma + num
   # soma += num
    print(f'soma dos numeros é {soma}')'''

#7
'''sexo = 0
contadorf = 0
contadorm = 0
qtde = 0
while sexo != 'sair':
    sexo = input('Digite o sexo "f" ou  "m": ')
    if sexo == 'f':
       contadorf += 1 
    elif sexo == 'm':
        contadorm +=1

    qtde = contadorf + contadorm
    print(f'A quantidade de homens foram {contadorm} e a quantidade de mulheres foram {contadorf}, a quantidade total foi {qtde}')'''
