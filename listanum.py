def gerar_lista():
    while True:
        # Menu de opções para escolher o que gerar
        print("\nMENU DE OPÇÕES")
        print("1 - Números pares")
        print("2 - Números ímpares")
        print("3 - Múltiplos de um número específico")
        print("0 - Sair")

        # Recebe a escolha do usuário
        opcao = int(input("Escolha uma opção: "))

        # Se digitar 0, encerra o programa
        if opcao == 0:
            print("Saindo... Valeu por usar o programa!")
            break

        # Define o intervalo de números (início e fim)
        inicio = int(input("Digite o número inicial do intervalo: "))
        fim = int(input("Digite o número final do intervalo: "))

        # Gera os pares
        if opcao == 1:
            resultado = [n for n in range(inicio, fim+1) if n % 2 == 0]

        # Gera os ímpares
        elif opcao == 2:
            resultado = [n for n in range(inicio, fim+1) if n % 2 != 0]

        # Gera os múltiplos do número escolhido
        elif opcao == 3:
            divisor = int(input("Digite o número divisor: "))
            resultado = [n for n in range(inicio, fim+1) if n % divisor == 0]

        # Caso escolha inválida
        else:
            print("Opção inválida! Tente novamente.")
            continue

        # Mostra o resultado final
        print("Resultado:", resultado)


# Executa o menu
gerar_lista()
