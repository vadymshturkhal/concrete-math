def descend_power(number, m):
    if m < 0:
        return number
    if m == 0:
        return 1

    return number * descend_power(number - 1, m - 1)
    
n = 3

sum_ = 0
for k in range(1, n + 1):
    sum_ = sum_ + descend_power(number=-2, m=k) / k

print(sum_)
