print(" ** CALCULANDO SUA MEDIA ** ")

av1 = float(input("Insira sua nota da AV1: "))
av2 = float(input("Insira sua nota da AV2: "))
avd = float(input("Insira sua nota da AVD: "))


def media():
    med = av1 + av2 + avd / 3

    if med > 6:
        print("Você foi aprovado com nota maior que a média.")
    elif med == 6:
        print("Você foi aprovado mas está na média.")
    elif med == 5:
        print("Você foi reprovado com média 5")
    elif med < 5:
        print("Sua média está abaixo de 5, por favor procure a lista de disciplinas elegíveis para segunda chance.")


media()
