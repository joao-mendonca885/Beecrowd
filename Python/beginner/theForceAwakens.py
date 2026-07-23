# -*- coding: utf-8 -*-

def eh_lightsaber(matriz, i, j):
    if matriz[i-1][j-1:j+2] != [7, 7, 7]:
        return False
    if matriz[i+1][j-1:j+2] != [7, 7, 7]:
        return False
    if matriz[i][j-1] != 7 or matriz[i][j+1] != 7:
        return False
    return True
            
l, c = map(int, input().split())
matriz = []
linha = []
for p in range(l):
    linha = list(map(int, input().split()))
    matriz.append(linha)
x = 0
y = 0
achou = False
for linhas in range(l):
    if achou: break
    for colunas in range(c):
        if matriz[linhas][colunas] == 42:
            if linhas == l-1 or colunas == c-1 or linhas == 0 or colunas == 0:
                continue
            achou = eh_lightsaber(matriz, linhas, colunas)
            if achou:
                x = linhas+1
                y = colunas+1
                break
print(f"{x} {y}")  
            