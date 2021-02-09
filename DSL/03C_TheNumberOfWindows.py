def main():
    n, q = map(int, input().split())
    (*a,) = map(int, input().split())
    (*x,) = map(int, input().split())
    for xi in x:
        i, s, ans = 0, 0, 0
        for j in range(1, n + 1):
            s += a[j - 1]
            while s > xi:
                s -= a[i]
                i += 1
            ans += j - i
        print(ans)


main()
