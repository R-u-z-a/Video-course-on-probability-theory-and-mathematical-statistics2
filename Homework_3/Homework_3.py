# Задача 1
# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 230, 24, 57, 55, 70, 75, 65, 84, 90, 150
#
# Используя только встроенные питоновские функции и структуры данных (т.е. без библиотек numpy, pandas и др.),
# посчитайте (несмещённое) среднее квадратичное отклонение для данной выборки.

# Ответ: 47.34795214

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

import seaborn as sns

salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 230, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# Среднее квадратичное отклонение:
a = 0
for item in salary:
    a = a + item
MO = a / len(salary)
print("Математическое ожидание:", MO)

# Смещенная и несмещенная оценки дисперсии:

a = 0
for item in salary:
    a = a + ((item - MO) ** 2)
QO = (a / len(salary)) ** 0.5
print("Квадратичное отклонение:", QO)

a = 0
for item in salary:
    a = a + ((item - MO) ** 2)
D_biased = a / len(salary)
D_unbiased = a / (len(salary) - 1)
print("Смещенная дисперсия:", D_biased)
print("Несмещенная дисперсия:", D_unbiased)

# проверим вычисления через встроенные библиотеки
au = np.array(salary)
print("Математическое ожидание:", au.mean())
print("Квадратичное отклонение:", au.std(ddof=0))
print("Смещенная дисперсия:", au.var())
print("Несмещенная дисперсия:", au.var(ddof=1))


