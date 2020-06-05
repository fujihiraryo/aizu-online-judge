S = input()
N = int(input())
for n in range(N):
    *w, = input().split()
    a, b = int(w[1]), int(w[2])
    if w[0] == 'replace':
        r = w[3]
        S = S[:a] + r + S[b + 1:]
    if w[0] == 'reverse':
        S = S[:a] + S[a:b + 1][::-1] + S[b + 1:]
    if w[0] == 'print':
        print(S[a:b + 1])
