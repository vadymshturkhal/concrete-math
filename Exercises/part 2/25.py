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
