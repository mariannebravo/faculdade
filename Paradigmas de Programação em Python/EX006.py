# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("Escolha um numero: "))


def isNegative():
    if num < 0:
        print("O numero escolhido eh negativo.")
    else:
        print("O numero escolhido eh positivo.")


isNegative()
