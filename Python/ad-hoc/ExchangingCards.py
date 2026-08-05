


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    la = set(map(int, input().split()))
    lb = set(map(int, input().split()))
    if len(la) >= len(lb):
        qtd = lb - la
    else:
        qtd = la - lb
    print(len(qtd))

    
    