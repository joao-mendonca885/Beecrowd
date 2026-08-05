# -*- coding: utf-8 -*-

#B - numero de bancos
#N - numero de titulos de divida
#segunda linha - reserva monetaria de cada um dos bancos - quanto cada banco tem
# as n proximas linhas o banco D deve V ao banco C
while True:
    b, n = map(int, input().split())
    if b == 0 and n == 0:
        break
    reservaMonetaria = list(map(int, input().split()))
    for _ in range(n):
        d, c, v = map(int, input().split())
        reservaMonetaria[d-1] -= v
        reservaMonetaria[c-1] += v
    if any(valor < 0 for valor in reservaMonetaria):
        print("N")
    else:
        print("S")