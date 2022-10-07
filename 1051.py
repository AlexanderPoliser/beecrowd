entry = float(input())

if entry <= 2000:
    print("Isento")
elif entry <= 3000:
    income_tax = (entry - 2000) * 0.08
    print(f"R$ {income_tax:.2f}")
elif entry <= 4500:
    income_tax = (entry - 3000) * 0.18 + (1000 * 0.08)
    print(f"R$ {income_tax:.2f}")
elif entry > 4500:
    income_tax = (entry - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print(f"R$ {income_tax:.2f}")
