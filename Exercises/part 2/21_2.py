def Tn(n: int):
    if n < 0:
        return 0
    
    return (1 + (-1)**n) // 2

def Sn(n):
    return (-Tn(n) + n + 1) // 2

def Un(n):
    return (-2 * Tn(n) - Sn(n) + (n + 1)**2) / 2


n = 4345
sum_ = 0
for k in range(n + 1):
    sum_ += (-1)**(n-k) * k**2

print(sum_)
print(Un(n))
