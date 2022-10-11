entry = int(input())

for i in range(entry):
    A, B, C = [float(x) for x in input().split(" ")]
    weighted_avg = ((A * 2) + (B * 3) + (C * 5)) / 10
    print(f"{weighted_avg:.1f}")
