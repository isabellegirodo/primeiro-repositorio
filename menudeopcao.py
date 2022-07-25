#####################################################################
#
# O programa: menudeopcao.py 
# Desenvolvido por Isabelle G. Girodo
# Data: 25/07/2022
#
#####################################################################

from math import factorial

print('\n\t\t-[BEM VINDO AO PROGRAMA MENU DE OPÇÕES]-\n')

def inteiroNumber():
    while True:
        try:
            def enterData():
                número = int(input('\n\t-- Digite um número positivo? '))
                return número
            coeffic = enterData()
            
            while coeffic <= 0:
                print('\n\t-[ Não use [Número Inteiro Negativo] ou igual [Zero]--Ok! ]')
                coeffic = enterData()
                
            print('\t**[ O [Número Inteiro Positivo]:',coeffic,'é um [Número] válido! ]**\n')
            return coeffic
                         
        except ValueError as err:
            print('\n\t-[Atenção!]:',err)
            print('\t-DIGITE UM [NOVO NÚMERO INTEIRO POSITIVO NA PRÓXIMA INSTRUÇÃO -- OK! ]\n')
                                        
num = inteiroNumber()

opcao = 0
while opcao != 7:
    print('''Selecione uma das opções:
    [1] Dobro
    [2] Raiz Quadrada
    [3] Par ou ímpar
    [4] Fatorial
    [5] Tabuada
    [6] Triplo
    [7] Finalizar o programa''','\n')
    
    print('Qual é a sua opção? ')
    opcao = inteiroNumber()
    
    if opcao == 1:
        dobro = num * 2
        print(f'O dobro de {num} é {dobro}\n')
    elif opcao == 2:
        raiz = num ** (1/2)
        print(f'A raiz quadrada de {num} é {raiz}\n')
    elif opcao == 3:
        if num % 2 == 0:
            print(f'O número {num} é par\n')
        if num % 2 == 1:
            print(f'O número {num} é ímpar\n')
    elif opcao == 4:
        fat = factorial(num)
        print(f'O fatorial é {fat}\n')
    elif opcao == 5:
        for t in range(1,11):
            print(f'{num} x {t} = {num * t}\n')
    elif opcao == 6:
        triplo = num * 3
        print(f'O triplo de {num} é {triplo}\n')
    elif opcao == 7:
        print('Sair do programa\n')
    elif opcao > 7:
        print('Opção inválida.Digite novamente!\n')

print('\n\t-[Programa Encerrado]-\n')
input('\n\t\t tecle [ENTER] para sair-OK!')

