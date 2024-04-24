# criar um conversor com as funções:
# converte de milhas para metros dado que 1 millha = 1609, 34 metros
# converte colheres de manteiga para gramas dado que 1 colher = 14 gramas

def metros_em_milhas(metros):
    """ converte metros em milhas """
    milhas=metros / 1609.34
    return(milhas)
  
def colheres_para_gramas(colheres):
    """ converte colheres em gramas """
    return colheres * 14
  

if __name__ == "__main__":
    print("Este módulo não é para ser usado directamente!")
