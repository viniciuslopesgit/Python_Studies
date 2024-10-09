#Recolhe o preço do primeiro produto
print("Preço do primeiro produto")
num1 = int(input())

#Recolhe o preço do segundo produto
print("Preço do segundo produto")
num2 = int(input())

#Recolhe o preço do terceiro produto
print("Preço do terceiro produto")
num3 = int(input())

#Cálcula o resultado final
total = num1 + num2 + num3
res = (total) * 10 / 100


#Imprime o resutlado final
print(f"Resultado com 10% de desconto aplicado: {total - res}")