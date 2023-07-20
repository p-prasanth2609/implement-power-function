def power(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a
    p = power(a, b // 2, c)
    if b % 2 == 0:
        return (p * p) % c
    else:
        return (p * p * a) % c

a = int(input())
b = int(input())
c = int(input())
print(power(a, b, c))
