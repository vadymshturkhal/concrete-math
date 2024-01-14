n = 3
mul_ = 1
for j in range(1, n + 1):
    for k in range(j, n + 1):
        mul_ = mul_ * j * k
print(mul_)

def formula(n):
    first_squared = 1
    second_squared = 1

    for k in range(1, n + 1):
        first_squared = first_squared * k
    
    first_squared = first_squared**2

    for k in range(1, n + 1):
        second_squared = second_squared * k**2
    
    return first_squared * second_squared

print(formula(n))
