def harmonic(n):
    if n <= 0:
        return 0

    return 1 / n + harmonic(n - 1)

n = 4
def formula(n):
    return -(harmonic(n - 1) + 1) / n + 1

sum_ = 0

for k in range(n):
    sum_ += harmonic(k) / ((k + 1) * (k + 2))

print(sum_)
print(formula(n + 1))
