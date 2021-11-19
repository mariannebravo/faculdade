# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F -Feminino, M -Masculino, Sexo Inválido.

sex = str(input("Insira seu sexo:"))


def whichSex():
    if sex == 'f':
        print("Seu sexo eh feminino")
    elif sex == 'm':
        print("Seu sexo eh masculino")
    else:
        print("INVALIDO")


whichSex()
