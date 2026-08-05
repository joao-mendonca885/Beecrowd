hi, mi, hf, mf = map(int, input().split())

startTotalMinutes = hi * 60 + mi
endTotalMinutes = hf * 60 + mf

durationMinutes = endTotalMinutes - startTotalMinutes

if durationMinutes <= 0:
    durationMinutes += 24 * 60

durationHours = durationMinutes // 60
durationMinutes = durationMinutes % 60

print(f"O JOGO DUROU {durationHours} HORA(S) E {durationMinutes} MINUTO(S)")


