print ("### CALCULADORA PYTHON ###")

def adicao (num1, num2):
    soma = num1 + num2
    return soma

print("Resultado da soma: ", adicao(16, 9))

def subtracao (num1, num2):
    subtracao = num1 - num2
    return subtracao

print("Resultado da subtração: ", subtracao(89,33 ))

def divisao (num1, num2):
    if num2 == 0:
        return "Não é possível dividir por zero!"
    else:
        divisao = num1 / num2
        return divisao

print("Resultado da Divisão: ", divisao(90, 3 ))

def raiz_quadrada (num):
    if num < 0:
        return "Não existe raiz real de número negativo!"
    else:
        raiz = num ** 0.5
        return raiz

print("Resultado da Raiz Quadrada: ", raiz_quadrada(81))