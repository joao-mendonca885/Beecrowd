# -*- coding: utf-8 -*-

while True:
    try:
        l, c = map(int, input().split())
        for linha in range(0,l):
                linhas = list(map(int, input().split()))
                if 2 in linhas:
                    colunaDeDois = linhas.index(2)
                    linhaDeDois = linha
                if 1 in linhas:
                    colunaDeUm = linhas.index(1)
                    linhaDeUm = linha               
        distancia = abs(linhaDeUm - linhaDeDois) + abs(colunaDeUm - colunaDeDois)
        print(distancia)
    except EOFError:
        break   