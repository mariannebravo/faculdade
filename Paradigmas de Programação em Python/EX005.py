# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Escolha um numero: "))
num2 = int(input("Escolha outro numero: "))


def check():
    if num1 > num2:
        print("O primeiro numero eh maior que o segundo.")
    elif num2 > num1:
        print("O segundo numero eh maior que o primeiro")
    elif num1 == num2:
        print("Os numeros escolhidos sao iguais")


check()
