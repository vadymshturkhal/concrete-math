"""
    1) P(k from K) c * a[k] = c**(len(K)) * P(k from K) a[k]
"""

K = [1, 2, 3, 4]

# 1
c = 3
mul_ = 1
for k in K:
    mul_ = c * mul_ * k

print(mul_)

c = 3
mul_ = 1
for k in K:
    mul_ = mul_ * k

print(mul_ * c**(len(K)))
print()

# 2
K = [1, 2, 3, 4]
B = [5, 6, 7, 8]

mul_ = 1
for k in range(len(K)):
    mul_ = mul_ * K[k] * B[k]
print(mul_)

mul_ = 1
for k in range(len(K)):
    mul_ = mul_ * K[k]

for k in range(len(B)):
    mul_ = mul_ * B[k]
print(mul_)
