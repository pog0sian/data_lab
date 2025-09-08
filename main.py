import time
import matplotlib.pyplot as plt
import sympy as sp
import random

# 1 вариант
# Задание 1
# 1) Сортировка
# 2) O(n^2) - квадратичная сложность алгоритма

def foo(a):
    start = time.perf_counter()
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    end = time.perf_counter()
    return end - start

sizes = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
times = []

for size in sizes:
    arr = [random.randint(-100, 100) for _ in range(size)]
    t = foo(arr)
    times.append(t)

plt.plot(sizes, times, marker='o')
plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (сек)')
plt.title('Зависимость времени работы от размера входных данных')
plt.grid(True)
plt.show()

# Задание 2

# O(n) — линейный алгоритм
def min_max_linear(array):
    min_val = array[0]
    max_val = array[0]
    for i in array:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    return min_val, max_val

# O(n^2) — через сортировку пузырьком
def min_max_sort(array):
    arr = array.copy()
    for i in range(len(arr), 0, -1):
        for j in range(1, i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr[0], arr[-1]

sizes = [100, 500, 1000, 2000, 4000]
times_linear = []
times_sort = []

for size in sizes:
    arr = [random.randint(-100, 100) for _ in range(size)]
    start = time.perf_counter()
    min_max_linear(arr)
    times_linear.append(time.perf_counter() - start)

    start = time.perf_counter()
    min_max_sort(arr)
    times_sort.append(time.perf_counter() - start)

plt.plot(sizes, times_linear, marker='o', label='O(n) линейный')
plt.plot(sizes, times_sort, marker='o', label='O(n²) сортировка')
plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (сек)')
plt.title('Сравнение алгоритмов поиска min/max')
plt.legend()
plt.grid(True)
plt.show()

# Задание 3

N = sp.Symbol('N')

T1 = N**2 - N - 10
T2 = 4*N + 40

solution = sp.solve(sp.Eq(T1, T2), N)

# Фильтрация положительных решений, потому что размер массива не может быть отрицательным
valid_solutions = [sol for sol in solution if sol > 0]

print("Положительные решения уравнения T1 = T2:", valid_solutions)

# Задание 4

sizes = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
times_list = []
times_dict = []

for size in sizes:
    # Список
    lst = list(range(size))
    start = time.perf_counter()
    for _ in range(size):
        del lst[-1]
    times_list.append(time.perf_counter() - start)

    # Словарь
    dct = {i: i for i in range(size)}
    start = time.perf_counter()
    for key in range(size-1, -1, -1):
        del dct[key]
    times_dict.append(time.perf_counter() - start)

plt.plot(sizes, times_list, marker='o', label='Список (del)')
plt.plot(sizes, times_dict, marker='o', label='Словарь (del)')
plt.xlabel('Размер структуры данных')
plt.ylabel('Время удаления всех элементов (сек)')
plt.title('Сравнение производительности del для списка и словаря')
plt.legend()
plt.grid(True)
plt.show()

# Задание 5

sizes = [1000, 5000, 10000, 20000, 40000, 80000]
times_list = []
times_set = []

for size in sizes:
    data = list(range(size))
    search_element = -1

    # Список
    start = time.perf_counter()
    for _ in range(100):
        _ = search_element in data
    times_list.append((time.perf_counter() - start) / 100)

    # Множество
    data_set = set(data)
    start = time.perf_counter()
    for _ in range(100):
        _ = search_element in data_set
    times_set.append((time.perf_counter() - start) / 100)

plt.plot(sizes, times_list, marker='o', label='Список (in)')
plt.plot(sizes, times_set, marker='o', label='Множество (in)')
plt.xlabel('Размер структуры данных')
plt.ylabel('Время поиска одного элемента (сек)')
plt.title('Сравнение производительности оператора in для списка и множества')
plt.legend()
plt.grid(True)
plt.show()
