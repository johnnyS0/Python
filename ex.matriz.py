matriz = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5,]
linha = 0
coluna = 0

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        matriz[linha][coluna]= int(input("informe o número da posição " + str(linha) + " " + str(coluna) + ": "))

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        if(str(linha) == str(coluna)):
            print("[",matriz[linha][coluna],"]", end='')
        else:
            print("[ ]", end='')
    
    print()
