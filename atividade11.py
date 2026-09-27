nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

frequencia = float(input("Digite a frequência (%): "))
financeiro = int(input("Situação financeira (1-Regular / 0-Pendente): "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and frequencia >= 75 and financeiro == 1:
    print("Aprovado")
else:
    print("Reprovado")

    if media < 7:
        print("Motivo: média abaixo de 7.")

    if frequencia < 75:
        print("Motivo: frequência abaixo de 75%.")

    if financeiro == 0:
        print("Motivo: pendência financeira.")



