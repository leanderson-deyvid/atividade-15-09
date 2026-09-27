distancia = float(input("Digite a distância da viagem (km): "))
consumo = float(input("Digite o consumo do carro (km/L): "))
preco = float(input("Digite o preço da gasolina por litro: R$ "))

litros = distancia / consumo
gasto = litros * preco

print("Litros necessários:", litros)
print("Gasto com combustível: R$", gasto)



