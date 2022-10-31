def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

common_divisor = gcd(365,100)
print(common_divisor)
