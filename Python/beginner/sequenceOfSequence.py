# -*- coding: utf-8 -*-

def impressao(Ncaso, qtdNum, sequencia):
    palavra = 'numero' if qtdNum == 1 else 'numeros'
    print(f"Caso {Ncaso}: {qtdNum} {palavra}")
    print(*sequencia)


lista = []
while True:
        linha = int(input())
        if linha == -1:
            break
        lista.append(linha)
    


for Ncaso, nf in enumerate(lista, start=1):
        sequencia = []
        for i in range(0, nf+1):
            for numero in range(0, max(1, i)):
                sequencia.append(i)
        qtdNum = len(sequencia)
        impressao(Ncaso, qtdNum, sequencia)
        print()
        
        
        

        
        
