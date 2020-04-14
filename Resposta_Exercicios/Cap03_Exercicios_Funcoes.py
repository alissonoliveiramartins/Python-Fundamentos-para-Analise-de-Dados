# ## Exercícios - Métodos e Funções


# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números      

def pares():
    return [par for par in range(0,21,2)]

pares()
        

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string


def maiusculas(string):
    return string.upper()

maiusculas('alisson')


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def adicionar(lista, elemento1, elemento2):
    lista.append(elemento1)
    lista.append(elemento2)
    return lista

adicionar([1,2,3],4,5)


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos


def exercicio4(arg, *args):
    print(f'1º Argumento é {arg}')
    for i in range(len(args)):
        print(f'{i}º Argumento é {args[i]}')


exercicio4('alisson')
print()
exercicio4('alisson','oliveira','martins')



# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
soma = lambda num1, num2: num1+num2

soma(2,3)



# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; #Variavel Local
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 ); #Variavel Global 
print ("Fora da função o total é: ", total)


# #No 1º 'print' ele pede para imprimir a variavel 'total' que esta sendo ultizada dentro da função para armazenamento da soma
# #no 2º 'print' ele pede para imprimir a variavel 'total' que foi atribuida no comerco da questão


# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda fah: (9/5)* fah + 32, Celsius)
print (list(Fahrenheit))


# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário
dict1 = {'key1': 1,
        'key2' : 2}
dir(dict1)
'''
TODOS OS METODOS : 
dict1.clear()
dict1.copy()
dict1.fromkeys()
dict1.get()
dict1.items()
dict1.keys()
dict1.pop()
dict1.popitem()
dict1.setdefault()
dict1.update()
dict1.values()
'''

# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
import pandas as pd
dir(pd)



# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
import pandas as pd
file_name = "binary.csv"

def retornaArq(file):
    arquivo = pd.read_csv(file)
    print(arquivo)
    return arquivo.describe()

    
retornaArq(file_name)  



# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
