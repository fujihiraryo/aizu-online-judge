from collections import defaultdict
import heapq


string = input()
count = defaultdict(int)
for char in string:
    count[char] += 1

chars = []
queue = []
for i, key in enumerate(count.keys()):
    chars.append(key)
    heapq.heappush(queue, (count[key], i))

if len(chars) == 1:
    print(len(string))
    exit()

n = 2 * len(chars) - 1
left = [None] * n
right = [None] * n
k = len(chars)
while len(queue) > 1:
    x, i = heapq.heappop(queue)
    y, j = heapq.heappop(queue)
    left[k] = i
    right[k] = j
    heapq.heappush(queue, (x + y, k))
    k += 1

_, i = queue.pop()
code = [None] * n
code[i] = 0
stack = [i]
while stack:
    i = stack.pop()
    if left[i] is not None:
        code[left[i]] = code[i] + 1
        stack.append(left[i])
    if right[i] is not None:
        code[right[i]] = code[i] + 1
        stack.append(right[i])

ans = 0
for i, c in enumerate(chars):
    ans += code[i] * count[c]
print(ans)
