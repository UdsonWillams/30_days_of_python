# Existem 4 tipos de collections em python nativamente
# Obviamente por meio de libs podem ser utilizadas mais
# como também temos a liberdade de criação.

#Listas, Dicionarios, Set, e Tuplas
# Dia 4 fala mais sobre as listas.

# criamos listas de 2 formas

lista1 = list()
lista2 = []
# utilizamos o metodo len() para verificar o tamanho de uma lista.
# metodo bastante utilizado, e diferente de outras linguagens chamamos
# ele, no lugar de chamar lista1.len(), chamamos len(lista1)
print(len(lista1))

# listam podem salvar tipos diferentes em sua estrutura
# por ex, lista1 = ["a", 2, [], {"dict": "dict"}]
# e esses valores são acessados facilmente com um 
# for ou uma especificação lista[0]

# forma interessante de desempacotar uma lista
# utilizando o comando *variavel, 
# que é reconhecido como uma lista.
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
# verificando itrens em uma lista
print("teste" in lista1)
# adicionando valor em uma lista
lista1.append("valor")
