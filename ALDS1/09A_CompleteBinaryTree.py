n = int(input())
(*heap,) = map(int, input().split())
for i in range(n):
    print(f"node {i+1}:", end=" ")
    print(f"key = {heap[i]},", end=" ")
    if i > 0:
        print(f"parent key = {heap[(i-1)//2]},", end=" ")
    if i * 2 + 1 < n:
        print(f"left key = {heap[i*2+1]},", end=" ")
    if i * 2 + 2 < n:
        print(f"right key = {heap[i*2+2]},", end=" ")
    print("")
