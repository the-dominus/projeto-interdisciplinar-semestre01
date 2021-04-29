# 001 - 28.04.2021 - 23h45
# 1° - Converter de decimal para binário, octal ou Hexadecimal
# 2° - Pegar o decimal e dividir por 2 
# 3° - Dependendo da base escolhida divdir por 2, 8 ou 16 a parte inteira e armazenar o resto
print("==============================================================\n")
print("Escolha para qual base você quer converter o numero decimal.\n")

print(" Digite 'B' ou 'b' para binario.\n Digite 'O' ou 'o' para Octal.\n Digite 'H' ou 'h' para Hexadecimal\n")
print("==============================================================\n")

option = str(input("Digite uma opção de conversão de base: "))

if option == "B" or option == "b":
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

elif option == "O" or option == "o":
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


elif option == "H" or option == "h":

    decimal = int (input("\nDigite o número em decimal: "))
    print("==============================================================")

    print("\nFunção nativa do Python para validação dos cálculos desenvolvidos pelo grupo:",hex(decimal))


    hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

    acum = []

    while decimal > 0:
        acum.append(hex[(decimal % 16)])

        decimal = decimal // 16
    
        for i in range(len(acum)-1,-1,-1):

            hexa = "".join(reversed(acum))

# Foi inserida na variável hexa uma função que junta todos os valores do array (JOIN) e então inverte 
# a ordem dos valores, um sort ao contrário. Reversed é uma função exclusiva de arrays.

    print("\nO valor em hexadecimal calculado em aritmética é:", hexa)
    print("\n==============================================================")

    input()

else:
    print("==============================================================")

    print("O valor de base digitado não existe! ")

    print("==============================================================")

    
