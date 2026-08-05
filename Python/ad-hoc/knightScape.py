

# -*- coding: utf-8 -*-

# the pawn move one square to any direction, WITHOUT GOING BACK

# 1 tem peao
def conversao(pos):
    letras = "abcdefgh"
    col = letras.index(pos[1])
    lin = int(pos[0]) - 1
    posicao = (lin, col)
    return posicao


def possiveisMovimentos(k):
    pos = list(conversao(k)) # retorna [3, 3]
    lin = pos[0]
    col = pos[1]
    movimentos = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    Rmov = []
    for dx, dy in movimentos:
        mc = (lin + dx, col + dy)
        if any(x < 0 or x > 7 for x in mc):
            continue
        else:
            Rmov.append(mc)
    return Rmov
def ataque(peoes):
    movimentos = [(-1, 1), (-1, -1)]
    ap = set()
    for peao in peoes:
        x = peao[0]
        y = peao[1]
        for dx, dy in movimentos:
            xAtaque = x + dx
            yAtaque = y + dy
            if xAtaque < 0 or xAtaque > 7 or yAtaque < 0 or yAtaque > 7:
                continue
            else:
                ap.add((xAtaque, yAtaque))
    return ap

nteste = 1
while True:
    cont = 0
    k = input() # supondo que k == 4d
    if int(k[0]) == 0:
        break
    peoes = []
    for c in range(8):
        peao = input()
        peoes.append(conversao(peao))
    posicoesK = possiveisMovimentos(k)
    posicoesDeAtaque = ataque(peoes)
    for pos in posicoesK:
        if pos in posicoesDeAtaque:
            continue
        else:
            cont += 1
    print(f"Caso de Teste #{nteste}: {cont} movimento(s).")
    nteste += 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    