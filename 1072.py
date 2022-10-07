x = int(input())
count_in = 0
count_out = 0

for i in range(x):
    value = int(input())
    if value < 0 or value > 20:
        count_out += 1
    elif value <= 10 or value <= 20:
        count_in += 1

print(f"{count_in} in")
print(f"{count_out} out")
