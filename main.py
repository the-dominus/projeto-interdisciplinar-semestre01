# 001 - 28.04.2021 - 23h45
# 1° - Converter de decimal para binário
# 2° - Pegar o decimal e dividir por 2 
# 3° - Sempre divdir por 2 a parte inteira e armazenar o resto


print("==============================================================")
decimal = int (input("Digite o número em decimal: "))
print("==============================================================")
print("\nFunção nativa do Python para validação dos cálculos desenvolvidos pelo grupo:",bin(decimal))

binario = ""
acum = []

while decimal > 0:
    resto = int(decimal % 2)

    decimal = decimal // 2
    
    acum.append(str(resto))

# Foi inserida na variável binário uma função que junta todos os valores do array (JOIN) e então inverte 
# a ordem dos valores, um sort ao contrário. Reversed é uma função exclusiva de arrays.
binario = binario.join(reversed(acum))

print("\nO valor em binário calculado em aritmética é:", binario)
print("\n==============================================================")
