# Dicionarios :D
# Coleção não ordenada, e pariada(possui chave,valor)

# criando um dicionario
dict1 = {}
dict2 = dict()

dict1 = {"chave": "valor", "chave2": "valor2"}
# notar os : entra os 2, sendo chave: valor 
# diferente dos sets que são só {"", "", ""}

# possivel utilizar o metodo len()
# mas ele  retorna o valor total de chaves.
assert len(dict1) == 2

# Acessando os valores
# Podemos acessar de duas formas 1°
dict1["chave"]
assert dict1["chave"] == "valor"
# porem se a chave não existir é retornado uma exceção.

# 2° forma é utilizando o metodo .get()
print(dict1.get("teste"))
# o bom do get é que ele não da erro se a chave não existir
# retornando o valor None, que é por padrão, tbm podendo
# se colocar outro valor como padrão, ex.:
print(dict1.get("teste", "A chave teste não existe!"))

# Podemos atualizar um dicionario de 2 formas também
# 1 ° forma
dict1["chave"] = "valor_1"
assert dict1["chave"] == "valor_1"
# dessa forma voce tem que instanciar um novo dict com a chave
# a ser atualizada, caso a chave não exista, ela é adicionada
# ao dicionario.
dict1.update({"chave": "valor_2"})
assert dict1["chave"] == "valor_2"

# possivel pegar os valores das chaves do dicionario
# ou apenas dos valores.
# ex.:

print(dict1.keys())
print(dict1.values())

# tbm é possivel transformar o dicionario numa lista de tuplas
# com o metodo .items() a logica é ordenar os valores,
# e eles não ficaram mais como chave e valor, 
# mas ficaram juntos, [("chave", "value1")]
print(dict1.items())
