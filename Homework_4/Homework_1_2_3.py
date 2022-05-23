import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

# Задача № 1

# Задача № 2

# 2. О случайной непрерывной равномерно распределенной величине B известно,
# что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная,
# что левая граница равна 0.5?
# Если да, найдите ее.

# Решение

a = 0.5
Dx = 0.2

# Применим формулу дисперсии и матиматического ожидания

# Отсюда

b = (12 * Dx) ** a + a

print(b)

# среднее значение будет соответствовать математическому ожиданию
Mx = (a + b) / 2
print(Mx)

samples = np.random.uniform(a, b, size=100)
print(samples)

# математическое ожидание через numpy
print(samples.mean())


# выборочная дисперсия (несмещённая) от выборки через numpy:
print(samples.var(ddof=1))

# Задание № 3

