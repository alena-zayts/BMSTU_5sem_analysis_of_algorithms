# # !/usr/bin/python
# # -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# import matplotlib.ticker as ticker

count = [1, 2, 4, 8, 16, 20, 24, 30, 32]

trace = [13.361 for i in range(9)]
paralltrace = [13.554, 8.102, 5.149, 3.736, 3.905, 4.72, 4.966, 4.28, 4.77]

fig, ax = plt.subplots()

# Что бы шаг по оси x был не стандартным,
# А массивом count.
plt.xticks(count)

ax.plot(count, trace, label="Стандартная трассировка")

ax.plot(count, paralltrace, label="Метод параллельной трассировки лучей")

ax.scatter(count, paralltrace, c='deeppink')

ax.scatter([1, 32], [13.361, 13.361], c='blue')


ax.legend()
ax.grid()
ax.set_xlabel('Количество потоков')
ax.set_ylabel('Время (с)')

plt.show()
