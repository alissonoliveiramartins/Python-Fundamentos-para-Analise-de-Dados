
# ## Exercícios Cap02

# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.


lista1 = []
for i in range(1,11):
    lista1.append(i)
print(lista1)


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela


lista2 = [1 , 'a' , 3.14 , ('alisson', 'oliveira') , [1,2,3] ]
print(lista2)


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string


string1 = 'Alisson '
string2 = 'Oliveira'
string3 = string1+string2
print(string3)


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla


tupla = (1, 2, 2, 3, 4, 4, 4, 5)
tupla.count(4)


# Exercício 5 - Crie um dicionário vazio e imprima na tela


dict1 = {}
print(dict1)


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela



dicionario1 = {'nome': 'Alisson', 'sobrenome' : 'Oliveira', 'idade' : 23 }
print(dicionario1)


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

dicionario1['sexo'] = 'masculino'



# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.



dicionario2 = {'chave1': [1,2], 'chave2': 1, 'chave3': 2}
print(dicionario2)



# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

lista3 = ['string' , (1,'str') , {'chave1':1, 'chave2':2} , 3.14]
print(lista3)


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'



frase[0:18]


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
