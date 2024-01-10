# First sum
def sum_minus_one(n: int):
    if n < 0:
        return 0
    
    if n % 2 == 0:
        return 1
    
    return 0

print(sum_minus_one(1249124124))
print(sum_minus_one(1249124121))
