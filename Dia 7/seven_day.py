# Sets
# Set é uma coleção de itens.
# A definição matematica de um set, tbm pode defini-lo
# em python, os elementos não são ordenados e não
# indexados. Cada elemento também precisa ser unico.

# criando um set
# set é uma palavra reservada.
# não é possivel setar um set com {} vazio, ele seria um dict
set_dict = {}
assert type(set_dict) == dict
sett = {"1", "2"}
sett2 = set()
assert type(sett) == type(sett2)

# usar loops para acessar itens especificos.

# possivel usar o len(), o operator in tbm é possivel.
# É possivel add mais itens com o metodo .add()

# É possivel atualizar o set, inclusive passando
# uma lista dos vaalores que queremos adicionar
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
assert "potato" in fruits
assert "cabbage" in fruits

# tbm é possivel remover intens usando o .remove()
fruits.remove("potato")
assert "potato" not in fruits
fruits.remove("cabbage")
assert "cabbage" not in fruits
# o metodo .pop tbm pode ser chamado, mas removeria um valor 
# aleatorio do set
removed = fruits.pop()
print(removed)
# tbm é possivel deleta-lo com o Del
del vegetables
try:
    print(vegetables)
except NameError:
    print("SET FOI EXCLUIDO")

# É possivel criar uma lista de um set
# ou um set de uma lista, porem o set será com valores unicos
lista = ["a", "b", "c"]
seet = set(lista)
assert "b" in seet

# tbm é possivel comparar 2 sets e retornar os valores
# que estao nos 2 sets com o metodo .intesection()

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2))

# tbm é possivel comparar 2 sets e retornar os valores
# que os 2 possuem de diferentes.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1))
print(st1.difference(st2)) # como st2 so tem 2 valores ele n é printado

