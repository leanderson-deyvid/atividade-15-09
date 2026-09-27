num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Escolha a operação: "))

if operacao == 1:
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacao == 2:
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacao == 3:
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacao == 4:
    resultado = num1 / num2
    print("Resultado:", resultado)

else:
    print("Operação inválida.")




