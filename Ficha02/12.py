def menu():
    while True:
        print(f"\nMenu de Opção:")
        print("1. Criar")
        print("2. Atualizar")
        print("3. Eliminar")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ")

        if (opcao == '1'):
            print("\n -> Opção selecionada: Criar")
        elif (opcao == '2'):
            print("\n -> Opção selecionada: Atualizar")
        elif (opcao == '3'):
            print("\n -> Opção selecionada Eliminar")
        elif (opcao == '4'):
            print("\n -> Saindo do programa...")
            break
        else:
            print("\n -> Opção Inválida. Por favor, escolha uma opção válida.")

menu()
