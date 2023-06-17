# Tupla

# COleção de difenrentes tipos de dados que são ordenados
# ou seja, possuem um index, e são imutaveis.

# criando uma tupla
tupla1 = ()
tupla2 = tuple()
# tbm da pra fazer algo do tipo
tupla3 = "", 
assert type(tupla3) == tuple
# como é ordenada possui um index
assert type(tupla3[0]) == str

# é possivel acessar seu index por meio do metodo
# .index(), fazer slicing(fatiamento), utiliza do
# metodo len(), parecido com uma list() mas imutavel

# Não é possivel apagar qualquer item de uma tupla
# Mas é possivel deletar a tupla inteira com o del

del tupla1
try:
    print(tupla1)
except NameError:
    print("TUPLA FOI EXCLUIDA")

