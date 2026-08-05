# -*- coding: utf-8 -*-
# N numero de bolas
# B numero de bolas ainda na bag
# b lista do valor das bolas que permaneceram na bag

import sys
input = sys.stdin.readline
#tive que usar sys.stdin.readline para conseguir passar no teste do TLE, 
# pois o input() nao estava conseguindo ler a entrada rapidamente
while True:
    N, B = map(int, input().split())
    if N == 0 and B == 0:
        break
    remainBag = list(map(int, input().split()))
    diferencas = set()
    lista = set(range(0, N+1))
    for a in range(len(remainBag)):
        for b in range(a, len(remainBag)):
            valorA = remainBag[a]
            valorB = remainBag[b]
            diferencas.add(abs(valorA-valorB))
    ehV = all(n in diferencas for n in lista)
    if ehV:
        print("Y")
    else:
        print("N")
        
     
        
            
        
            