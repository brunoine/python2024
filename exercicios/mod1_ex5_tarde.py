# Pergunte ao utilizador qual a temperatura da água e que devolva o estado físico da mesma (sólido, líquido ou gasoso)

valor = eval(input("qual a temperatura da água? \n"))

estado = 'sólido' if valor <=0 else \
'líquido' if valor < 100 else \
'gasoso' 

print(estado)
