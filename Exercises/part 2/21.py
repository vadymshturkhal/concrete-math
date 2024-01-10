# First sum
def sum_minus_one(n: int):
    if n < 0:
        return 0
    
    if n % 2 == 0:
        return 1
    
    return 0

def sum_minus_one_formula(n: int):
    if n < 0:
        return 0
    
    return (1 + (-1)**n) // 2

n = 131216
print(sum_minus_one(n))
print(sum_minus_one_formula(n))
