# -*- coding: utf-8 -*-
# T -> numero da expressao e numero de players
# x e y sao iguais a z
#N -> nome do player(até 50 caracteres)
# E o indice da posicao escolhida
# R = operacao escolhida
# Se todo player passar print("You Shall All Pass!")
# Se nenhum player passar print noneshall pass
# n1_n2 = n3
while True:
    try:
        t = int(input())
        for i in range(0, t):
            lista = list(input.split())
            listanum = []
            for valores in lista:
                if valores.isdigit():
                    listanum.append(valores)
            n1, n2, n3 = map(int, listanum)