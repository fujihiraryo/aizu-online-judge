def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


K = int(input())
count = 0
for i in range(K):
    n = int(input())
    if is_prime(n):
        count += 1
print(count)
