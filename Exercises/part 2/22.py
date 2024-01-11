n = 3
sum_ = 0

a = [1, 2, 3]
b = [4, 5, 6]

for j in range(0, n ):
    for k in range(j + 1, n):
        sum_ += (a[j] * b[k] - a[k] * b[j])**2

print(sum_)

sum_a = 0
for k in range(0, n):
    sum_a += a[k]**2

sum_b = 0
for k in range(0, n):
    sum_b += b[k]**2

sum_ab = sum_a * sum_b

sum_minus = 0
for k in range(0, n):
    sum_minus += a[k] * b[k]

sum_minus = sum_minus**2

print(sum_ab - sum_minus)