n = 445
sum_ = 0

for k in range(1, n + 1):
    sum_ += (2*k + 1) / (k * (k + 1))

print(sum_)

def harmonic(n):
    if n <= 0:
        return 0

    return 1 / n + harmonic(n - 1)

def formula(n):
    return 2 * harmonic(n) + (1 / (n + 1)) - 1

print(formula(n))
