X, Y, Z = [float(x) for x in input().split(" ")]
if X >= Y and X >= Z:
    A = X
    B = Y
    C = Z

if Y >= X and Y >= Z:
    A = Y
    B = X
    C = Z

if Z >= X and Z >= Y:
    A = Z
    B = X
    C = Y

if A < B + C:
    if A ** 2 == (B ** 2) + (C ** 2):
        print("TRIANGULO RETANGULO")
    elif A ** 2 > (B ** 2) + (C ** 2):
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    if A == B and B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")