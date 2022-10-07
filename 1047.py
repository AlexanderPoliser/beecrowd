entry = [int(i) for i in input().split(" ")]
start_h = entry[0]
start_m = entry[1]
end_h = entry[2]
end_m = entry[3]

total_hours = end_h - start_h
total_minutes = end_m - start_m

if total_minutes < 0:
    total_minutes += 60
    total_hours -= 1

if total_hours < 0:
    total_hours += 24

if total_hours == 0 and total_minutes == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {total_hours} HORA(S) E {total_minutes} MINUTO(S)")