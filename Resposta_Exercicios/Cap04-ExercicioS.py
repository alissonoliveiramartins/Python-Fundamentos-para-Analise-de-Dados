# ## Exercícios 

# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.


lst = [1,2,3]

print(list(x**3 for x in lst))


# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)

list(map(lambda palavra :[palavra.upper(), palavra.lower(), len(palavra)], palavras))


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]

transposta=[ [trans[i] for trans in matrix] for i in range(2)]
print(transposta)


# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

def qua(n):
    return n**2 
def cub(n):
    return n**3

funcao = [qua , cub]

for num in lista:
    print(list(map(lambda x: x(num) , funcao )))
    

# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]

print(list(map( pow, listaA, listaB)))


# In[ ]:


# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)


# In[62]:


print(list(filter(lambda x:  x < 0, range(-5, 5))))


# In[63]:


# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]


# In[64]:


print(list(filter(lambda x: x in a,b)))


# In[67]:


# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!
import datetime
print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

#https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python
import time
print(time.strftime("%d/%m/%Y %H:%M"))


# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

dict(zip(dict1, dict2.values()))


# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


print([num for indice, num in enumerate(lista) if indice > 5])


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
