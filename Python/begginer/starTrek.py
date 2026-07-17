# -*- coding: utf-8 -*-
n = int(input())
stars = list(map(int, input().split()))

atacadas = set()
i = 0

while 0 <= i <= n - 1:
    era_impar = (stars[i] % 2 == 1)   # PARIDADE ANTES de roubar

    if stars[i] > 0:                  # rouba se houver
        stars[i] -= 1
        atacadas.add(i)

    if era_impar:                     # decide pela paridade ORIGINAL
        i += 1
    else:
        i -= 1

print(f"{len(atacadas)} {sum(stars)}")