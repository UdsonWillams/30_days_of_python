# Loops de repetição - For
# Loops de repetição, como o nome já diz
# É um bloco de codigo que vai ficar sendo repetido
# Durante a execução do codigo.
# No python o loop for é feito utilizando a palavra for

# O python tem uma diferença pra outras linguagens por que
# Seu for é basicamente utilizado para percorrer objetos
# Iteraveis, possuem o dunder method __iter__ implementado.
# Por mais que consiga ser utilizado de forma mais tradicional
# passando o valor de parada das interações, ele ainda é mais 
# utilizado sendo um foreach.

# metodo mais tradicional
for i in range(0, 11): # lembrando que o range é excludente, vai de 0 a 10, excluindo o 11.
    print(f"numero: {i}")

# metodo de interação com interaveis(listas, typlas, dicionarios, etc.)
numeros = [0, 1, 2, 3, 4, 5]
print("for em interavel")
for numero in numeros:
    print(f"numero: {numero}") 

# existe uma forma interessante de usar o for com dicts
dici = {"nome": "udson", "idade": "17", "genero": "masculino"}
for i in dici:
    print(i)
for k, v in dici.items():
    print(f"chave: {k} - valor: {v}")
# e tbm pode ser utilizado com o enumerate
for number, chave in enumerate(dici):
    print(f"numero: {number} - chave: {chave}")

# tbm possui o break e o continue que o loop while tem
# Break - usado para sair do loop.
# Continue - usado para passar a interação atual do loop 
# para a proxima

# tbm é possivel utilizar o else como pos for
for i in range(0, 11):
    print(f"numero: {i}")
else:
    print("for finalizado")
