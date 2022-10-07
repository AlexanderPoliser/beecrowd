x = int(input())
y = int(input())
sum = 0

if x > y:
    for value in range(y+1, x):
        if value % 2 != 0:
            sum = sum + value
else:
    for value in range(x+1, y):
        if value % 2 != 0:
            sum = sum + value
print(sum)
