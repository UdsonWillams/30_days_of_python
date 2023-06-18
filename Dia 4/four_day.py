#Strings
# qualquer dado entre uma, duas ou três aspas são strings
#'' or "" or """"""

string_1 = ''
string_2 = ""
string_3 = """
    Ola meu amigo
"""
print(string_3)

# formato antigo de formatação de strings python
# %s string
# %d integers
# %f float numbers
# ex.:
first_name = 'Udson'
last_name = 'Willams'
language = 'Python'
formated_string = 'Eu %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
############################
# o novo formato se utiliza da func .format()
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print("string com .format()" + formated_string)
# e nas versoes 3.6 pra frente se utiliza o F string
a = 4
b = 3
# utiliza do f antes da string
# e as variaveis são possiveis de serem utilizadas.
print(f'{a} + {b} = {a +b}') 
print(f'{a} - {b} = {a - b}')

# as strings em python são como as listas
# uma string, ex.: varv = "valor" pode ser assedado como varv[0] ou varv[1]
