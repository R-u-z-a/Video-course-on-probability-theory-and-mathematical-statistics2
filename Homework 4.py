# Производятся выстрелы по мишени.
# Вероятность попадания в мишень при одном выстреле равна 0.01.
# Сколько выстрелов нужно сделать чтобы быть уверенным с вероятностью 0.9, что хотя бы 6 раз будет совершено попадание?
#
# Подсказка:
# 1) "Вероятность попасть k раз при n выстрелах" - на какое распределение это похоже?
# 2) А если нам нужна вероятность P(X >= k), а не P(X = k)?
# 3) Здесь предстоит немножко покодить.

import numpy as np
from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

p = 0.01
k = 6
n = 6
P = 0

while (P < 0.9):
    k = 0
    P_0 = combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))
    k = 1
    P_1 = combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))
    k = 2
    P_2 = combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))
    k = 3
    P_3 = combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))
    k = 4
    P_4 = combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))
    k = 5
    P_5 = combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))

    pop = P_0 + P_1 + P_2 + P_3 + P_4 + P_5
    P = (1 - pop)
    print(f"Итерация:{n}, P(X<6)={pop},P(X>=6)={P}")
    n = n + 1  # к следующей итерации
