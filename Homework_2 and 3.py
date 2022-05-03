from math import factorial

# Найдем общее число случаев (С из 60 по 3).

n = int(60 * 59 * 58 / 6)

# Благоприятное число случаев (C из 50 по 3)
m = int(50 * 49 * 48 / 6)

# Тогда искомая вероятность Р=m/n
P = m / n
print(P)
# Тогда искомая вероятность (С из 50 по 2)•(С из 10 по 1)
m = int(50 * 49 / 2) * 10
print(m / n)


# Либо решим ее немного по другому.

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


m = combinations(60, 3)

n = combinations(50, 3)
print(m, n)

p3 = n / m
print('Вероятность того, что знает 3 карты', p3)

# для случая, когда знает 2 билета и еще 1 билет не знает

x = combinations(50, 2) * combinations(10, 1)
print(x)
p2 = x / m
print(p2)

