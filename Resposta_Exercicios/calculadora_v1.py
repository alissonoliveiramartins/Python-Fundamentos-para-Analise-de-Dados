# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def menu():
    opcao = ['Soma','Subtração','Multiplicação','Divisão']
    print('Selecione o numero da operaçao desejada: \n')
    for i in range(1, len(opcao)+1):
        print(f'{i} - {opcao[i-1]}')
    print()

soma = lambda x,y : x+y
subtracao = lambda x,y : x-y
multiplicacaoo = lambda x,y : x*y
divisao = lambda x,y : x/y

if __name__ == '__main__' :
    menu()
    op = int(input('Digite sua opcão (1/2/3/4): '))
    n1 = int( input( 'Digite o primeiro número: '))
    n2 = int( input( 'Digite o segundo número: '))
    if op == 1:
        print(f'{n1} + {n2} = {soma(n1,n2)}')

    elif op == 2:
        print(f'{n1} - {n2} = {subtracao(n1,n2)}')

    elif op == 3:
        print(f'{n1} * {n2} = {multiplicacao(n1,n2)}')

    elif op == 4:
        print(f'{n1} / {n2} = {divisao(n1,n2)}')

    else:
        print('Opção invalida. ')
    
        
        
            
              
    
