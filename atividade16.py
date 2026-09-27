valor = int(input("Digite o valor do saque: R$ "))

if valor <= 0:
    print("Valor inválido.")

elif valor % 10 != 0:
    print("Não é possível formar esse valor com as notas disponíveis.")

else:
    notas100 = valor // 100
    resto = valor % 100

    notas50 = resto // 50
    resto = resto % 50

    notas20 = resto // 20
    resto = resto % 20

    notas10 = resto // 10

    print(notas100, "notas de R$100")
    print(notas50, "notas de R$50")
    print(notas20, "notas de R$20")
    print(notas10, "notas de R$10")





