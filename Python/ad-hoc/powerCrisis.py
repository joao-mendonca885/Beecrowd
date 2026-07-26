# -*- coding: utf-8 -*-


#m = 3 -> de m em m apaga cidades
#n = 10 -> numero de cidades
#lista = list(range(1, n+1))
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = 1
while n != 0:
    n = int(input())
    if n == 0:
        break
    apagados = [None] * n # preenchendo uma lista com none de tamanho n
    m = 0
    while apagados[n-1] != 13: #enquanto o ultimo nao for 13
        m = m + 1 #comecando com m == 1
        apagados = [] #lista das cidades apagadas por ordem
        totais = list(range(1, n+1)) #lista das cidades
        c = 0 #c comecando sempre com 0 para remover o 1 elemento
        cont = 0 #contador de quantas cidades foram apagadas
        while len(apagados) != n: #enquanto todos as cidades nao estiverem apagadas
            apagados.append(totais[c])
            totais.remove(totais[c])
            if apagados[cont] == 13: #se apagou a cidade 13
                if cont == n-1: # se a ultima cidade apagada foi a 13
                    print(m)
                    break
                else:
                    apagados = [None] * n
                    break
            if c + m - 1 == 0:
                c = 0
            elif len(totais) != 0:
                c = (c + m - 1) % len(totais)           
            cont = cont + 1     
        
    