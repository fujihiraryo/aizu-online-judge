def lcs(s, t):
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    for i in range(m):
        prev = dp[:]
        for j in range(n):
            if s[i] == t[j]:
                dp[j + 1] = prev[j] + 1
            elif prev[j + 1] < dp[j]:
                dp[j + 1] = dp[j]
    return dp[n]


q = int(input())
for _ in range(q):
    s = input()
    t = input()
    print(lcs(s, t))
