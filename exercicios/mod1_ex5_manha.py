# Exercicio

#calcula o total e a média de 4 valores

v1 = input('Digite 1 valor: ')
v2 = input('Digite outro: ')
v3 = input('Digite mais 1: ')
v4 = input('Digite o ultimo: ')

soma = eval(v1) + eval(v2) + eval(v3) + eval(v4) 

media = soma/4

print(f"o total é: {soma}; a média é: {media:.2f}")
