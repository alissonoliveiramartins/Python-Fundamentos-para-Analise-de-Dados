#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios Cap02

# In[ ]:


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.


# In[3]:


lista1 = []
for i in range(1,11):
    lista1.append(i)
print(lista1)


# In[ ]:


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela


# In[5]:


lista2 = [1 , 'a' , 3.14 , ('alisson', 'oliveira') , [1,2,3] ]
print(lista2)


# In[ ]:


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string


# In[17]:


string1 = 'Alisson '
string2 = 'Oliveira'
string3 = string1+string2
print(string3)


# In[ ]:


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla


# In[10]:


tupla = (1, 2, 2, 3, 4, 4, 4, 5)
tupla.count(4)


# In[ ]:


# Exercício 5 - Crie um dicionário vazio e imprima na tela


# In[11]:


dict1 = {}
print(dict1)


# In[12]:


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela


# In[13]:


dicionario1 = {'nome': 'Alisson', 'sobrenome' : 'Oliveira', 'idade' : 23 }
print(dicionario)


# In[ ]:


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela


# In[14]:


dicionario1['sexo'] = 'masculino'


# In[ ]:


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.


# In[15]:


dicionario2 = {'chave1': [1,2], 'chave2': 1, 'chave3': 2}
print(dicionario2)


# In[ ]:


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.


# In[16]:


lista3 = ['string' , (1,'str') , {'chave1':1, 'chave2':2} , 3.14]
print(lista3)


# In[8]:


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'


# In[18]:


frase[0:18]


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
