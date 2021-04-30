# 001 - 28.04.2021 - 23h45
# 1° - Converter de decimal para binário, octal ou Hexadecimal
# 2° - Pegar o decimal e dividir por 2 
# 3° - Dependendo da base escolhida divdir por 2, 8 ou 16 a parte inteira e armazenar o resto

while True:

    print("==============================================================\n")
    print("Escolha para qual base você quer converter o numero decimal.\n")

    print(" Digite 'B' para Binário.\n Digite 'O' para Octal.\n Digite 'H' para Hexadecimal.\n")
    print("==============================================================\n")

    option = str(input("Digite uma opção de conversão de base: ")).upper()

    if option == "B":
        decimal = int (input("\nDigite o número em decimal: "))
        print("==============================================================")

        print("\nFunção nativa do Python para validação dos cálculos desenvolvidos pelo grupo:",bin(decimal))



        acum = []

        while decimal > 0:
            resto = int(decimal % 2)

            decimal = decimal // 2
        
            acum.append(str(resto))

    # Foi inserida na variável binário uma função que junta todos os valores do array (JOIN) e então inverte 
    # a ordem dos valores, um sort ao contrário. Reversed é uma função exclusiva de arrays.
        binario = "".join(reversed(acum))

        print("\nO valor em binário calculado em aritmética é:", binario)
        print("\n==============================================================")

    elif option == "O":
        decimal = int (input("\nDigite o número em decimal: "))
        print("==============================================================")

        print("\nFunção nativa do Python para validação dos cálculos desenvolvidos pelo grupo:",oct(decimal))



        acum = []

        while decimal > 0:
            resto = int(decimal % 8)

            decimal = decimal // 8
        
            acum.append(str(resto))

    # Foi inserida na variável octal uma função que junta todos os valores do array (JOIN) e então inverte 
    # a ordem dos valores, um sort ao contrário. Reversed é uma função exclusiva de arrays.
        octal = "".join(reversed(acum))

        print("\nO valor em octal calculado em aritmética é:", octal)
        print("\n==============================================================")


    elif option == "H":

        decimal = int(input("\nDigite o número em decimal: "))
        print("==============================================================")

        print("\nFunção nativa do Python para validação dos cálculos desenvolvidos pelo grupo:",hex(decimal))

        # Criada uma lista contendo todos os quinze valores em hexadecimal.
        # Quando fizermos o cálculo, basta procurar o valor do resto da divisão nessa lista.
        hexa = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        
        # Acumulador dos valores que representarão o valor em Hexadecimal.
        acum = []

        while decimal > 0:

            # Insere na lista "acum" o valor que está na lista "hexa" no index equivalente ao valor do resto.
            resto = decimal % 16
            valorHexa = hexa[resto]
            acum.append(valorHexa)

            decimal = decimal // 16   

        
        hexadecimal = "".join(reversed(acum))

    # Foi inserida na variável hexa uma função que junta todos os valores do array (JOIN) e então inverte 
    # a ordem dos valores, um sort ao contrário. Reversed é uma função exclusiva de arrays.

        print("\nO valor em hexadecimal calculado em aritmética é:", hexadecimal)
        print("\n==============================================================")


    else:
        print("==============================================================")

        print("O valor de base digitado não existe! ")

        print("==============================================================")

    respostaStatus = input("Deseja continuar no programa? Digite 'S' para continuar: ").upper()

    if respostaStatus != "S":
        break