count = 0
sum = 0
avg = 0

for i in range(6):
    value = float(input())
    if value > 0:
        count += 1
        sum += value
        avg = sum/count
print(f"{count} valores positivos")
print(f"{avg:.1f}")