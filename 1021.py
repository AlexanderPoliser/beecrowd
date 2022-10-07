value = float(input())

notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for note in notes:
    number_notes = int(value / note)
    print("{} nota(s) de R$ {:.2f}".format(number_notes, note))
    value -= number_notes * note
print("MOEDAS:")
for coin in coins:
    number_coins = int(round(value, 2) / coin)
    print("{} moeda(s) de R$ {:.2f}".format(number_coins, coin))
    value -= round(number_coins * coin, 2)