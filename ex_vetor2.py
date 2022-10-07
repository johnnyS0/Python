vetor = [0] * 5
cont = 0

for cont in range(0,50,1):
    vetor[cont] = int(input("informe o número da posição " + str(cont) + ": "))
    if (vetor[cont] % 2 == 0):
        vetor[cont] = vetor[cont] + (vetor[cont] * 0.02)
    else:
        vetor[cont] = vetor[cont] + (vetor[cont] * 0.05)


for cont in range(0,50,1):
    print(vetor[cont], end='' ";  ")
