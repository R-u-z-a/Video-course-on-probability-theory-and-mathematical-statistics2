# Задание № 1

# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

import numpy as np

salary = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
scoring = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]


def mean(l: list) -> float:
    """Среднее арифметическое."""
    return sum(l) / len(l)


def covariance(l1: list, l2: list, unbiased: bool = True) -> float:
    """Выборочная ковариация."""
    mean1 = mean(l1)
    mean2 = mean(l2)
    l = list(map(lambda x, y: (x - mean1) * (y - mean2), l1, l2))
    return sum(l) / (len(l) - int(unbiased))


print(covariance(salary, scoring))

np.cov(salary, scoring, ddof=1)

array = ([[3882.93333333, 10175.37777778],
          [10175.37777778, 33854.32222222]])


def variance(l: list, unbiased: bool = True) -> float:
    """Выборочная дисперсия."""
    mean_ = mean(l)
    l = list(map(lambda x: (x - mean_) ** 2, l))
    return sum(l) / (len(l) - int(unbiased))


def std(l: list, unbiased: bool = True) -> float:
    """Выборочное среднее квадратическое отклонение."""
    return variance(l, unbiased) ** 0.5


def corr(l1: list, l2: list) -> float:
    """Коэффициент корреляции Пирсона."""
    return covariance(l1, l2) / std(l1) / std(l2)


r = corr(salary, scoring)
print(r)

np.corrcoef(salary, scoring)
array = ([[1., 0.88749009],
          [0.88749009, 1.]])

# Задание № 2

# Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

from scipy import stats
from matplotlib import pyplot as plt

alpha = 0.05
n = len(salary)

t1 = stats.t.ppf(alpha / 2, df=n - 2)
t2 = stats.t.ppf(1 - alpha / 2, df=n - 2)

print(t1, t2)
# Получается, что у нас критичная область.

plt.style.use('seaborn-whitegrid')
# config InlineBackend.figure_formats = ['svg']

ox = np.linspace(-5, 5, 500)
oy = stats.t.pdf(ox, df=n - 1)

ox_left = np.linspace(ox[0], t1, 100)
oy_left = stats.t.pdf(ox_left, df=n - 1)

ox_right = np.linspace(t2, ox[-1], 100)
oy_right = stats.t.pdf(ox_right, df=n - 1)

plt.plot(ox, oy)
plt.fill_between(ox_left, oy_left, alpha=0.5, color='C0')
plt.fill_between(ox_right, oy_right, alpha=0.5, color='C0')

# Считаем значение статистики и проводим тест.

t = r * np.sqrt(n - 2) / np.sqrt(1 - r ** 2)
print(t)

# Статистика попала в критическую область, следовательно, гипотеза о равенстве нулю корреляции отвергается.
# Значит, зависимость между выборками значима.

# Задание № 3

# Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.

# Решение

# Требуется построить доверительный интервал для нормально распределённой случайной величины с неизвестной дисперсией

samples = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

n = samples.shape[0]
mean = samples.mean()
std = samples.std(ddof=1)

print(n, mean, std)

# Найдём квантили:


p = 0.95
alpha = 1 - p

t1 = stats.t.ppf(alpha / 2, df=n - 1)
t2 = stats.t.ppf(1 - alpha / 2, df=n - 1)

print(t1, t2)

# Итак, доверительный интервал:

print(mean + t1 * std / np.sqrt(n), mean + t2 * std / np.sqrt(n))
