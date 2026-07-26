# -*- coding: utf-8 -*-
# N numero de bolas
# B numero de bolas ainda na bag
# b lista do valor das bolas que permaneceram na bag


while True:
    N, B = map(int, input().split())
    if N == 0 and B == 0:
        break
    remainBag = list(map(int, input().split()))
    cont = 0
    for resultado in range(0, N+1):
        naoTemResultado = True
        for i in remainBag and naoTemResultado:
            for j in range(i, len(remainBag)):
                if abs(i - remainBag[j]) == resultado:
                    cont = cont + 1
                    NaoTemResultado = False
                    break
    if cont == N+1:
        print("Y")
    else:
        print("N")
     
        
            
        
            
        
            