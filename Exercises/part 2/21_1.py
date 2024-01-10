n = 551245

sum_ = 0 
for k in range(n + 1):
    sum_ += (-1)**(n - k) * k

def sum_minus_one_formula(n: int):
    if n < 0:
        return 0
    
    return (1 + (-1)**n) // 2

print(sum_)

# Formula
print((-sum_minus_one_formula(n) + n + 1) // 2)
