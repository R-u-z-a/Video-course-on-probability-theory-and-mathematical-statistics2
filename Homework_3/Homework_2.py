# Задача 2
# Найдите число выбросов в выборке из задачи 1.
# Для определения выбросов используйте методику как при построении “усов” в boxplot, однако, как и в задаче 1, пользоваться можно только встроенными функциями и структурами данных.

# Ответ: 2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
import seaborn as sns

# найдем медиану, первый и третий квартили, интерквартильное расстояние,

salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 230, 24, 57, 55, 70, 75, 65, 84, 90, 150]

salary_sorted = sorted(salary)
length = len(salary_sorted)
b = pd.Series(salary)
print(length)
print(salary_sorted)

# salary_sorted[length//2-1:length//2+1]

# ввиду того, что получили нечетную длину выборки, медиана будет посередине отсортированного массива
mas = salary_sorted[length // 2]
print("Середина отсортированного массива:", mas)

# med = (salary_sorted[length//2-1] + salary_sorted[length//2])/2
med = salary_sorted[length // 2]
print("Медиана:", med)

# первый квартиль
Q1 = salary_sorted[int(length // 4)]
print("Первый квартиль:", Q1)

# третий квартиль
Q3 = salary_sorted[int(length * 3 // 4)]
print("третий квартиль:", Q3)

print("Интерквартильное расстояние:", [Q1, Q3])

# проверим вычисления через встроенные библиотеки
print(b.mode())
b.quantile([0.25, 0.5, 0.75])

plt.hist(b, bins=16)
plt.show()

# найдем выборсы в выборке (используя для этого метод как при построении "усов" из boxplot)

# выборсы в выборке
iqr = Q3 - Q1
boxplot_range_low = Q1 - 1.5 * iqr
boxplot_range_high = Q3 + 1.5 * iqr

for i in range(len(salary)):
    if salary[i] < boxplot_range_low or salary[i] > boxplot_range_high:
        print(f'Выброс: сумма з/п {salary[i]} с индексом {i}')

# ОТОБРАЗИМ на графике усов
pd.DataFrame(b).boxplot()

# вычислим с использованием встроенных библиотек
# выборсы в выборке
df = pd.DataFrame(b)
q1 = b.quantile(0.25)
q3 = b.quantile(0.75)
iqr = q3 - q1
boxplot_range = (q1 - 1.5 * iqr, q3 + 1.5 * iqr)
outliers = df.loc[(b < boxplot_range[0]) | (b > boxplot_range[1])]
print(outliers)

# seaborn -- более симпатичная визуализация
sns.boxplot(df, orient='h')
plt.show()
