n = int(input())
lst = [input().split() for i in range(n)]
dict = {}
for op, s in lst:
    if op == "insert":
        dict[s] = 1
    if op == "find":
        try:
            if dict[s] == 1:
                print("yes")
        except:
            print("no")
