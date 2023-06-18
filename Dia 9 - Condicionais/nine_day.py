# Condicionais - if, else, elif.
# Em python ( como tbm em outras linguagens) o 
# IF é usado para checar algum condição. e executar algum bloco de codigo.
# ex.:
cond = "ola"
if cond:
    print(cond)

# Dai entra o else, que seria o contraponto do IF
# Caso a condição do if não seja valida, o else é chamado
# Ex.:
if cond == "oi":
    print(cond)
else:
    print(f"cond não é oi, é {cond}")

# E para finalizar tbm existe o Elif, chamado de else if 
# em outras lingugagens, executa o bloco de codigo com 
# outra verificação, antes de entrar no else
# Ex.:

if cond == "oi":
    print(cond)
elif cond == "tchau":
    print("tchau")
else:
    print(f"cond não é oi, e nem tchau, cond é {cond}")
