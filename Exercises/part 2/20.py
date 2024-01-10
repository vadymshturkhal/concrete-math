def harmonic(n):
    if n <= 0:
        return 0

    return 1 / n + harmonic(n - 1)

print(harmonic(n=2))

n = 3
first_value = (n + 1) * harmonic(n + 1) - n - 1
second_value = 0

for k in range(1, n + 1):
    second_value += harmonic(k)

print(first_value)
print(second_value)
