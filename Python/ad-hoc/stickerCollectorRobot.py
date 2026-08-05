


def achar_estado_inicial(matriz, currentStage):
    for linha in range(l):
        for coluna in range(c):
            if matriz[linha][coluna] in currentStage:
                posl = linha
                posc = coluna
                direcao = matriz[linha][coluna]
                return [posl, posc, direcao]

def dentro_e_pilar(posla, posca, l, c):
    return 0 < posla <= l and 0 < posca <= c and matriz[posla][posca] != "#"           


def ehEstrela(pos):
    if pos == "*":
        return True
    return False


def jogadas(matriz, l, c, comando, currentStage, posl, posc, direcao):
    if comando == "D": # vamos somente trocar a direcao em que ele está
        for indice in range (len(currentStage)):
            if currentStage[indice] == direcao:
                direcao = currentStage[(indice + 1) % 4]
                matriz[posl][posc] = direcao
                return 0
    elif comando == "E":
        for indice in range (len(currentStage)):
            if currentStage[indice] == direcao:
                direcao = currentStage[(indice - 1) % 4]
                matriz[posl][posc] = direcao
                return 0
    elif comando == "F":
        rumos = [[posl+1, posc],  # como se fosse uma matriz 4 x 2
                [posl, posc+1], 
                [posl-1, posc], 
                [posl, posc-1]]
        for indice in range(len(currentStage)):
            if currentStage[indice] == direcao:
                if dentro_e_pilar(rumos[indice][0], rumos[indice][1], l, c): #verifica se o movimento que vai fazer é possível
                    temp = matriz[rumos[indice][0]][rumos[indice][1]]
                    matriz[rumos[indice][0]][rumos[indice][1]] = direcao
                    matriz[posl][posc] = "*"
                    posl = rumos[indice][0]
                    posc = rumos[indice][1]
                    if ehEstrela(temp):
                        return 1
                else:
                    return 0



def resultados(matriz, l, c, comandos, currentStage, posl, posc, direcao):
    resultado = 0
    for comando in comandos:
        resultado += jogadas(matriz, l, c, comando, currentStage, posl, posc, direcao)
    return resultado



while True:
    l, c, n = map(int, input().split())
    if l == 0 and c == 0 and n == 0:
        break

    matriz = [[0 for i in range(c)] for _ in range (l)]

    for linha in range(l):
        matriz[linha] = list(input())

    comandos = list(input())
    currentStage = ["N", "L", "S", "O"]
    estadoInicial = achar_estado_inicial(matriz, currentStage)  #[posl, posc, direcao]
    posl = estadoInicial[0]
    posc = estadoInicial[1]
    direcao = estadoInicial[2] 
    print(resultados(matriz, l, c, comandos, currentStage, posl, posc, direcao))
