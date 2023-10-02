#Minha primeira Calculadora em python

def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b


def calculadora():
    print('Selecione uma operacao:')
    print('1. Soma')
    print('2. Subtracao')
    print('3. Multiplicacao')
    print('4. Divisao')

    escolha = input('Digite o numero da operacao desejada:')

    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outeo numero: '))

    if escolha == '1':
        print('Resultado: ', soma(num1, num2))
    elif escolha == '2':
        print('Resultado: ', subtracao(num1, num2))
    elif escolha == '3':
        print('Resultado: ', multiplicacao(num1, num2))
    elif escolha == '4':
        print('Resultado: ', divisao(num1, num2))
    else:
        print('Opcao Invalida!')
    
calculadora()
