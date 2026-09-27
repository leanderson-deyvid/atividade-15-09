peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

if peso <= 0 or altura <= 0:
    print("Peso ou altura inválidos.")
else:
    imc = peso / (altura * altura)

    print("Seu IMC é:", imc)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidade")




