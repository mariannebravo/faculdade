# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Insira uma letra: "))


def isConsonant():
    if letra == 'a':
        print("Essa letra eh uma vogal.")
    elif letra == 'e':
        print("Essa letra eh uma vogal")
    elif letra == 'i':
        print("Essa letra eh uma vogal")
    elif letra == 'o':
        print("Essa letra eh uma vogal")
    elif letra == 'u':
        print("Essa letra eh uma vogal")
    else:
        print("Essa letra eh uma consoante")


isConsonant()
