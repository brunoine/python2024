# exercicio 6
# apresente, separado por ++++, os quatro primeiros multiplos de um numero dado pelo utilizador 

N = eval(input('Digita um numero:'))

lista = []

for i in range(1, N+1):
  if N%i == 0:
    lista.append(i)
    
print(*lista[:4], sep = '+++')
