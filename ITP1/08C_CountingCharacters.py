S = open(0).read().lower()
a = [0 for i in range(26)]
for c in S:
    if ord(c) >= 97 and ord(c) <= 97 + 25:
        a[ord(c) - 97] += 1
for i in range(26):
    print('{} : {}'.format(chr(i + 97), a[i]))
