# Funções
# Oque é uma função? 
# São blocos de codigo reutilizavel, com foco em fazer certas tarefas.

# ex.:
def print_someting(valor):
    print("o valor passado foi: {}".format(valor))

# agora sempre que eu quiser printar um valor com esse exemplo
# eu utilizo da função.
print_someting("meu valor é de string.")
print_someting(15)

# é possivel fazer uma fnc dessa forma "sem parenteses"(com parenteses dps de um espaço)
# me parece algo sem sentido, mas da pra fazer, KKK
# def print_someting ():
#     print("o valor passado foi: {}".format())

# funções podem ou n retornar valores, caso retornem, precisam
# da palavra reservada return com o objeto de retorno.
def print_someting(valor):
    return print("o valor passado foi: {}".format(valor))
# essa func acima inclusive retorna uma outra função, a func print, que é builtin.

# essas func podem receber parametros que podem ser acessados dentro do escopo
# da func, nos exemplos acima eu passo um parametro que é o valor.
# esse parametro vai poder ser acessado e manejado, e ate retornado com outros 
# valores dentro da função.
# ex.:
def return_someting(valor):
    return valor + " valor adicionado"
print(return_someting("ola"))
# como eu fiz com o print_someting encadiei o retorno da func return_someting com o print.

# é possivel tbm ao chamar uma função utilizar do seus parametros para deixar mais 
# especifico oque queremos. ex.:
print(return_someting(valor="o valor é esse"))
# notemos que setei o parametro como uma variavel, isso é muito bom quando temos
# diversos parametros e precisamos setar cada coisa em seu lugar especifico.

# tbm podemos passar os valores em ordem dos parametros, mas geralmtente se
# existem muitos parametros pode ficar algo meio confuso.
# ex.:

def return_someting(valor1, valor2, valor3, valor4, valor5):
    return f"{valor1}" + " valor adicionado"
# aquio podemos chamar uma func dessa forma
return_someting(1, 2, 3, 4,5)
# por ser uma func simples fica fácil de entender, mas uma função maior
# ja seria mais complicado de entender qual parametro recebe oque.
# além de cada parametro podem esperar tipos diferentes e etc.
# ent o melhor seria algo assim
return_someting(valor1=1, valor2=2, valor3=3, valor4=4, valor5=5)

# os parametros tbm podem receber um valor padrão para o caso
# de ele ser necessario, mas não seja passado nda, por ex.:
def return_someting(valor1, valor2 = 2, valor3 = 2, valor4 = 2, valor5 = " valor 5"):
    return f"{valor1}" + " valor adicionado"

# mesmo com os default, deixei um sem nenhum default, ent pelo menos
# um valor deve ser passado, dessa forma abaixo retorna um erro.
#valor = return_someting()
valor = return_someting(1) # dessa forma o vlr foi passado.
assert valor is not None
print(valor)
