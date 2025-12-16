import numpy as np
import matplotlib.pyplot as plt

# Данные (можно заменить своими)
x = np.array([58, 85, 85, 85, 103, 127, 47])
y = np.array([161, 386, 386, 386, 535, 867, 73])

# Количество точек
n = len(x)

# Считаем суммы
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_xy = np.sum(x * y)

# Вычисляем коэффициенты
k = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - k * sum_x) / n

print(f"Уравнение прямой: y = {k:.3f}x + {b:.3f}")

# Строим график
plt.scatter(x, y, color="red", label="Точки")   # экспериментальные точки
plt.plot(x, k * x + b, color="blue", label=f"y = {k:.2f}x + {b:.2f}")  # аппроксимирующая прямая

plt.xlabel("x")
plt.ylabel("y")
plt.title("Линейная аппроксимация методом наименьших квадратов")
plt.legend()
plt.grid(True)
plt.show()
