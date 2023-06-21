# tbm fazem partes das funções 
# os parametros nomeados. mas coisas especificas, achei legal dividir
# pra falar um pouco deles em especifico.

# args
# podemos passar uma lista como argumento pra função utilizando o *
def return_someting(*args):
    return args
# a func vai receber os parametros como uma lista, com os valores que passamos dentro.
def soma_total(*args):
    return sum(args)

total = soma_total(1, 2, 3, 4, 5)
assert total == 15
print(total)
# isso funciona por que a func sum retorna a soma de um interavel
# e como falei, os argumentos passados se transformam em uma lista
# se olharmos bem passei os argumentos normais, sem utlkizar do list() ou []

# agora é uma lista dentro da func, temos que saber como usar e por que usar
# dessa funcionalidade do python, não podemos só criar funções dessa forma e
# passar inumeros parametros sem sentido.

# existe tbm a possiblidade dos key words arguments
# que são os argumentos nominados.
# ex.:
def soma_total(**kargs):
    return print(kargs)

# ja os argumentos nomeados, são um dicionario, aonde recebemos
# os valores passados na chamada da função.
soma_total(numero_1=1, numero2=2)

# podemos nomear os parametros depois da função feita, mas se
# caso a função não use os parametros passados, então não terá efeitos.
# ex.:
def soma_total(**kargs):
    assert type(kargs) == dict
    valor_a_retornar = kargs.get("numero2")
    print(valor_a_retornar)
    return valor_a_retornar

valor = soma_total(numero_1=1, numero2=2, numero3=3)
print(valor)
assert valor == 2
# dessa forma os kw numero_1 e numero3 não foram utilizados.
