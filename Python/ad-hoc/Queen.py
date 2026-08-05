#colunas: x
#linhas: y
while True:
    c1, l1, c2, l2 = map(int, input().split())
    if c1 == l1 and c1 == l2 and c2 == l2 and l2 == 0:
        break
    if l1 == l2 and c1 != c2: #mesma linha e colunas diferentes
        print("1")
    elif c1 == c2 and l1 != l2:#mesma coluna e linhas diferentes
        print("1")
    elif abs(l1-l2) == abs(c1-c2) and abs(l1-l2) != 0: #mesma diagonal e diferente posicao
        print("1")
    elif l1 == l2 and c1 == c2: #mesma posicao
        print("0")
    else:#o pior caso precisa de 2 movimentos
        print("2")