# Write a recursive program to get the sum of each digit in an integer. e.g. sumDigits(345) -> 12 or sumDigits(45) -> 9

def sumDigits(n):
    if n == 0:
        return 0
    return (n % 10 + sumDigits(int(n/10)))

new = sumDigits(12345)
print(new)

# help from GeeksforGeeks.org
