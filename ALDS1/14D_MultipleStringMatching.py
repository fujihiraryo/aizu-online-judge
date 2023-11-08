import bisect


def suffix_array(string):
    sa = [string[i : i + 1000] for i in range(len(string))]
    sa.sort()
    return sa


def search(sa, pattern):
    i = bisect.bisect_left(sa, pattern)
    return i < len(sa) and pattern in sa[i]


target = input()
sa = suffix_array(target)
for _ in range(int(input())):
    pattern = input()
    print(int(search(sa, pattern)))
