from math import factorial


# Будем использовать формулу комбинаторки

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


k = 52

i = 1
c1 = combinations(4, i)
c2 = combinations(k - 4, 4 - i)
a = c1 * c2
print(c1, c2, a)

i = 2
c1 = combinations(4, i)
c2 = combinations(k - 4, 4 - i)
b = c1 * c2
print(c1, c2, b)

i = 3
c1 = combinations(4, i)
c2 = combinations(k - 4, 4 - i)
c = c1 * c2
print(c1, c2, c)

i = 4
c1 = combinations(4, i)
c2 = combinations(k - 4, 4 - i)
d = c1 * c2
print(c1, c2, d)

print(a + b + c + d)

# Решим задачу другим способом
# Найдём вероятность противоположного события A` - среди четырёх вынутых карт нет дамы
# Общее число способов выбрать 4 карты из 52 равно числу сочетаний по 52 по 4

c = combinations(52, 4)

# Благоприятствующие события- число способов вынуть 4 карты из 48, среди которых нет дам

m = combinations(48, 4)

#  Вероятность противоположного события A

A = m / c
print(A)

# Вероятность события A, что появится хотя бы одна дама

print(1 - A)
