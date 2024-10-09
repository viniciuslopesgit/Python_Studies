#Recolhe o primeiro valor
print("Introduza o primeiro valor")
valor1 = int(input())

#Recolhe o segundo valor
print("Introduza o segundo valor")
valor2 = int(input())

valor1 = valor1 + valor2
valor2 = valor1 - valor2
valor1 = valor1 - valor2

print(f"Valor1: {valor1}")
print(f"Valor2: {valor2}")