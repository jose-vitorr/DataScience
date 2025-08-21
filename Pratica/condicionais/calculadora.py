# 4 operações básicas de uma calculadora
def soma(valor1, valor2):
    return valor1 + valor2

def subtracao(valor1, valor2):
    return valor1 - valor2

def multiplicacao(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2): 
    # fail fast: checar se o divisor é zero
    if valor2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return valor1 / valor2

# Função principal da calculadora
def calculadora(valor1, valor2, operacao):
    if operacao == 'soma':
        print("Resultado da soma:", soma(valor1, valor2))
        return soma(valor1, valor2)
    elif operacao == 'subtracao':
        print("Resultado da subtração:", subtracao(valor1, valor2))
        return subtracao(valor1, valor2)
    elif operacao == 'multiplicacao':
        print("Resultado da multiplicação:", multiplicacao(valor1, valor2))
        return multiplicacao(valor1, valor2)
    elif operacao == 'divisao':
        print("Resultado da divisão:", divisao(valor1, valor2))
        return divisao(valor1, valor2)
    else:
        return "Operação inválida. Use: soma, subtracao, multiplicacao ou divisao."
    
# Exemplo de uso
calculadora(10, 5, 'soma')
calculadora(10, 5, 'subtracao')
calculadora(10, 5, 'multiplicacao')
calculadora(10, 5, 'divisao')