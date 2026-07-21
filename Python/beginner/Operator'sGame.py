# -*- coding: utf-8 -*-
# T -> numero da expressao e numero de players
# x e y sao iguais a z
#N -> nome do player(até 50 caracteres)
# E o indice da posicao escolhida
# R = operacao escolhida
# Se todo player passar print("You Shall All Pass!")
# Se nenhum player passar print("None Shall Pass!")
# n1_n2 = n3
# if listanum[0] (operador aritmetico) listanum[1] == lista[2]--> condicao verdadeira
import operator

while True:
    try:
        operacoes = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        }
        lf = [] #lista que contem o nome, indice e operacao. Cada posicao é a pessoa em ordem
        listaSeparada = [] #lista dos numeros separados por indices
        t = int(input()) #qtd de testes
        for i in range(0, t):
            linha = input() #"3 4=5"
            linha = linha.replace("=", " ")#"3 4 5"
            lista = linha.split()#["3", "4", "5"]
            numeros = [int(x) for x in lista] #[3, 4, 5]
            listaSeparada.append(numeros)
        for i in range(0, t):
            nome, indice, operacao = input().split()# ["João", "3", "+"]
            dicionario = dict()
            dicionario["nome"] = nome
            dicionario["indice"] = int(indice) 
            dicionario["operacao"] = operacao
            lf.append(dicionario)
        qtd = 0 #qtd de pessoas erradas
        errados = [] #lista de pessoas erradas
        for c in range(0, t): 
            achou = False #achou ou nao achou pessoa errada
            if lf[c]["operacao"] == "I":
                for op in operacoes.values():# testa todas as posicoes para o indice escolhido
                    if op(listaSeparada[lf[c]["indice"] - 1][0],listaSeparada[lf[c]["indice"] - 1][1])  == listaSeparada[lf[c]["indice"] - 1][2]:
                        achou = True
                        break
            elif operacoes[lf[c]["operacao"]](listaSeparada[lf[c]["indice"] - 1][0],listaSeparada[lf[c]["indice"] - 1][1])  != listaSeparada[lf[c]["indice"] - 1][2]:
                achou = True
            if achou:
                qtd += 1
                errados.append(lf[c]["nome"])
        if qtd == 0:
            print("You Shall All Pass!")
        elif qtd == t:
            print("None Shall Pass!")
        else:
            print(" ".join(sorted(errados)))
    except EOFError:
        break
            