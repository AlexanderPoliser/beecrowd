entry = int(input())

for i in range(entry):
    value = int(input())
    if value % 2 == 0 and value > 0:
        print("EVEN POSITIVE")
    elif value % 2 == 0 and value < 0:
        print("EVEN NEGATIVE")
    elif value % 2 != 0 and value > 0:
        print("ODD POSITIVE")
    elif value % 2 != 0 and value < 0:
        print("ODD NEGATIVE")
    else:
        print("NULL")
