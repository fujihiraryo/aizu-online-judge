S = int(input())
h, S = S // 3600, S % 3600
m, s = S // 60, S % 60
print("{}:{}:{}".format(h, m, s))
