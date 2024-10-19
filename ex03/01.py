def main():
	while True:
		try:
			num1 = int(input("Enter the first value: "))
			num2 = int(input("Enter the second value: "))
			oper = input("Enter the simbol of the operation: ")

			resultado = num_calc(num1, num2, oper)

			continue_prog = input("Do you want to continue? (Enter y/n): ").lower()
			if (continue_prog == 'n'):
				print("Quiting program...")
				break
			elif (continue_prog != 'n' and continue_prog != 'y'):
				print("Invalid parameter...")
		except ValueError:
			print("Erro: Please, enter a valid numeric value.")


def num_calc(num1, num2, oper):
	if (oper == '+'):
		print(f"Result: {num1} + {num2} = {num1 + num2}")
	elif (oper == '-'):
		print(f"Result: {num1} - {num2} = {num1 - num2}")
	elif (oper == '*'):
		print(f"Result: {num1} * {num2} = {num1 * num2}")
	elif (oper == '/'):
		print(f"Result: {num1} / {num2} = {num1 / num2}")
	else:
		print("Invalid Operator")

if __name__ == "__main__":
	main()
