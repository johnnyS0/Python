vetor = [0] * 10
cont = 0

for cont in range(0,10,1):
    vetor[cont] = int(input("informe o número da posição " + str(cont) + ": "))

for cont in range(9,-1,-1):
    print(vetor[cont], end=''"; ")
