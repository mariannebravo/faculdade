# Insira 3 alturas e diga qual eh a maior ou se todas sao iguais

alt1 = float(input("Insira a altura da primeira pessoa:"))
alt2 = float(input("Insira a altura da segunda pessoa:"))
alt3 = float(input("Insira a altura da terceira pessoa:"))


def highestToLowest():
    if alt1 > alt2 and alt3:
        print("A altura da primeira pessoa eh a maior.")
    elif alt2 > alt1 and alt3:
        print("A altura da segunda pessoa eh a maior.")
    elif alt3 > alt1 and alt2:
        print("A altura da terceira pessoa eh a maior.")
    elif alt1 == alt2 and alt3:
        print("As alturas sao iguais.")


highestToLowest()
