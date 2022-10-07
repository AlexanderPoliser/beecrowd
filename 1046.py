entry = input().split()
start = int(entry[0])
end = int(entry[1])

if start < end:
    game_duration = end - start
    print(f"O JOGO DUROU {game_duration} HORA(S)")
else:
    game_duration = (24 - start) + end
    print(f"O JOGO DUROU {game_duration} HORA(S)")
