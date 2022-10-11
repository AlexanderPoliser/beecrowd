entry = int(input())

amount, count, r, s, c = 0, 0, 0, 0, 0

for test in range(entry):
    amount, type_animal = input().split()
    str(type_animal)
    count += int(amount)
    if type_animal == "R":
        r += int(amount)
    elif type_animal == "S":
        s += int(amount)
    elif type_animal == "C":
        c += int(amount)


calc_percent_bunny = float((c * 100)/count)
calc_percent_rat = float((r * 100)/count)
calc_percent_frog = float((s * 100)/count)

print(f"Total: {count} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {calc_percent_bunny:.2f} %")
print(f"Percentual de ratos: {calc_percent_rat:.2f} %")
print(f"Percentual de sapos: {calc_percent_frog:.2f} %")
