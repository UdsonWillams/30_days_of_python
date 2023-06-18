# Loops de repetição - While
# Loops de repetição, como o nome já diz
# É um bloco de codigo que vai ficar sendo repetido
# Durante a execução do codigo.
# No python o loop while é feito utilizando a palavra while

# while + condição gera um loop, ex.:

cond = True
while cond:
    print("Olá")
    cond = False

# Enquanto a confição do while for verdadeira ele vai
# executar o codigo dentro do seu escopo

# Com o bloco while, podemos adicionar um else ao final
# de sua execução
cond = True
while cond:
    print("Olá")
    cond = False
else:
    print("loop terminou")

# Mais duas interações são possiveis com o loop while
# Break - usado para sair do loop.
# Continue - usado para passar a interação atual do loop 
# para a proxima

# geralmente é usado um contador num loop while
# pra contabilizar as vezes que ele rodou e finalizar se der
# O valor da condição do while, nesse caso se ele for menor que 5.
contador = 1 
while contador < 10:
    if contador == 3:
        contador = contador + 1
        continue # continua a interação do loop pra proxima
    elif contador == 7:
        break # break finaliza o loop
    print(contador)
    contador = contador + 1

print("while finalizado.")
