# Modulos.

# Um módulo é um arquivo contendo um conjunto de códigos ou um 
# conjunto de funções que podem ser incluídas em um aplicativo. 
# Um módulo pode ser um arquivo contendo uma única variável,
# uma função ou uma grande base de código.

# importamos um modulo com a palavra reservada import.

import os

# podemos importar funcoes especificas de cada modulo
# ex.:
from my_module import soma # pode ser uma ou mais funções.
#from my_module import soma, divisao, subtracao
soma()

# podemos renomear o "valor" do modulo importado
# ex.:

from my_module import subtracao as SubT

SubT()

import string # builtin pouco explorado.
# TODO estudar builtin string.

print(string.ascii_lowercase)

from random import random, randint
print(random())   # Se não for passado nenhum parametro, retorna um valor entre 0 e 0.9999
print(randint(5, 20))

# Se olharmos bem, o randon e o randint são variaveis.
# dentro da seu modulo eles estão sendo instanciados por funções.
# Mas chegam a nos como variaveis, pois é possivel instanciar uma função
# Em uma variavel. 

# Ex.:
sub = SubT
sub()
