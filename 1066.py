count_pos = 0
count_neg = 0
count_odd = 0
count_even = 0

for i in range(5):
    value = int(input())
    if value % 2 == 0:
        count_even += 1
    if value % 2 == 1:
        count_odd += 1
    if value > 0:
        count_pos += 1
    if value < 0:
        count_neg += 1

print(f"{count_even} valor(es) par(es)")
print(f"{count_odd} valor(es) impar(es)")
print(f"{count_pos} valor(es) positivo(s)")
print(f"{count_neg} valor(es) negativo(s)")
