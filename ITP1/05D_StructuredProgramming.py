n = int(input())
a = []
for i in range(1, n + 1):
    if i % 3 == 0 or "3" in str(i):
        a.append(str(i))
print(" " + " ".join(a))
