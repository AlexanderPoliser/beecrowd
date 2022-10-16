k = 7

for i in range(1, 10, 2):

    for j in range(3):
        j = k - j
        print(f"I={i} J={j}")

    k += 2
