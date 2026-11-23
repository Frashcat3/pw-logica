while True:
    print("___ Calculadora ___\n" \
    "1- Somar \n"
    "2- Subtrair \n"
    "3- Multiplicar \n"
    "4- Dividir \n"
    "5- Sair \n")
    opcao = int(input("Escola uma opção: "))
    if opcao == 4:
        print("Encerrando calculadora...")
        break
    if opcao == 1:
        print("Você Escolheu Somar")
        break
    if opcao == 2:
        print("Você Escolheu Subtrair")
        break
    if opcao == 3:
        print("Você Escolheu Multiplicar")
        break
    else:
        print("Opção inválida")