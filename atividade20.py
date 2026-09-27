distancia = float(input("Digite a distância da corrida em km: "))
passageiros = int(input("Digite a quantidade de passageiros: "))
pico = int(input("A corrida acontece no horário de pico? (1 = sim / 0 = não): "))

if distancia <= 0 or passageiros <= 0:
    print("Dados inválidos.")
else:
    # Valor inicial
    valor = 5 + (distancia * 2)

    # 1. Horário de pico: acrescenta 30%
    if pico == 1:
        valor = valor * 1.30

    # 2. Mais de 3 passageiros: acrescenta R$ 10,00
    if passageiros > 3:
        valor = valor + 10

    # 3. Mais de 20 km: desconto de 10%
    if distancia > 20:
        valor = valor * 0.90

    # Resultado
    print(f"\nDistância: {distancia:g} km")
    print(f"Passageiros: {passageiros}")
    
    if pico == 1:
        print("Horário de pico: Sim")
    else:
        print("Horário de pico: Não")

    print(f"Valor da corrida: R$ {valor:.2f}")
