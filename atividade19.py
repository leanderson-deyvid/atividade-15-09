horas = float(input("Digite a quantidade de horas: "))

if horas <= 0:
    print("Quantidade de horas inválida!")
else:
    cadastrado = int(input("Cliente cadastrado? (1 = sim / 0 = não): "))

    if horas <= 1:
        valor = 10.00
    elif horas <= 3:
        valor = 20.00
    elif horas <= 5:
        valor = 30.00
    elif horas <= 8:
        valor = 40.00
    else:
        valor = 50.00

    # Desconto de 20% para clientes cadastrados
    # O desconto não se aplica para mais de 8 horas
    if cadastrado == 1 and horas <= 8:
        valor = valor * 0.80

    print(f"Valor final: R$ {valor:.2f}")
