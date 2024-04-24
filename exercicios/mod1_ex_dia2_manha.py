##
texto = input("insere uma palavra com a letra 'a': ")

print(len(texto))

texto.replace('a','')[::-1]


##
frase = input("escreve uma frase:")
# conta os espaços entre palavras, para o numero total de palavras da frase somamos 1 
frase.count(' ') +1


##
n=input("quantos números queres?")

lista = []
for i in range(5):
  valor = eval(input(f"introduz valor {i+1}: "))
  lista += [valor]
  
  
print(lista)

