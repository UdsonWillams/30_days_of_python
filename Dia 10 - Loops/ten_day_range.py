# É uma função que retorna numeros
# Ela recebe 3 parametros, inicio, fim e o "incremento"
# O padrão a função começa  com 0 e incrementa 1 por vez.
# Mas precisamos passar o final da interação.
# Ex.:
lista = list(range(11)) 
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2 argumentos indicam o inicio e o fim da sequencia. e o incremento caso não passado é o padrão = 1
sett = set(range(1, 11))
print(sett) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lista_incrementada = list(range(0,11,2))
print(lista_incrementada) # [0, 2, 4, 6, 8, 10]
sett_incrementado = set(range(0,11,2))
print(sett_incrementado) #  {0, 2, 4, 6, 8, 10}
