# First sum
def sum_minus_one(n: int):
    if n < 0:
        return 0
    
    if n % 2 == 0:
        return 1
    
    return 0

print(sum_minus_one(1249124124))
print(sum_minus_one(1249124121))

def sum_minus_one_formula(n: int):
    if n < 0:
        return 0
    
    return (1 + (-1)**n) // 2

print(sum_minus_one_formula(1249124124))
print(sum_minus_one_formula(1249124121))
