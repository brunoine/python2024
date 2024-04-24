# circulo.py

import math


class Circulo:

    # atributo (property) partilhado entre todas as instâncias da classe
    count_circulos = 0

    # método constutor
    # executado sempre que se cria um obejcto do tipo Circulo
    def __init__(self, raio):

        # Circulo.count_circulos += 1
        type(self).count_circulos += 1

        self.raio = raio  # cada instância tem a seu atributo (property)

    # método público
    def area(self):
        return round(math.pi * self._raio_ao_quadrado(), 2)

    # método privado
    def _raio_ao_quadrado(self):
        return self.raio ** 2
