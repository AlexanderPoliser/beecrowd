highest_value = 0
pos = 0

for i in range(100):
    value = int(input())
    if value > highest_value:
        highest_value = value
        pos = i

print(f"{highest_value}")
print(f"{pos + 1}")
