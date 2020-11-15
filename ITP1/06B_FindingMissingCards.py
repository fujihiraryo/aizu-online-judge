n = int(input())
cards = []
for i in range(n):
    m, n = input().split()
    cards.append((m, int(n)))
for m in ["S", "H", "C", "D"]:
    for n in range(1, 13 + 1):
        if (m, n) not in cards:
            print(m, n)
