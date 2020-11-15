W = input()
count = 0
while True:
    (*T,) = input().split()
    if T[0] == "END_OF_TEXT":
        break
    T = [t.lower() for t in T]
    count += T.count(W)
print(count)
