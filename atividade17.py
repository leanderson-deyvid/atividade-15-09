ladoA = float(input("Digite o lado A: "))
ladoB = float(input("Digite o lado B: "))
ladoC = float(input("Digite o lado C: "))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:

    if ladoA == ladoB and ladoB == ladoC:
        print("Triângulo Equilátero")

    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Triângulo Isósceles")

    else:
        print("Triângulo Escaleno")

else:
    print("Os valores não formam um triângulo.")

