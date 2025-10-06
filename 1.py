import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    return time.perf_counter() - start

sizes = [100, 200, 400, 800, 1600]
results = {'random': {'selection': [], 'quick': []},
           'sorted': {'selection': [], 'quick': []},
           'reversed': {'selection': [], 'quick': []}}

for size in sizes:
    arr_random = [random.randint(0, 10000) for _ in range(size)]
    arr_sorted = sorted(arr_random)
    arr_reversed = sorted(arr_random, reverse=True)

    # Случайные
    results['random']['selection'].append(measure_time(selection_sort, arr_random))
    results['random']['quick'].append(measure_time(quick_sort, arr_random))
    # Отсортированные
    results['sorted']['selection'].append(measure_time(selection_sort, arr_sorted))
    results['sorted']['quick'].append(measure_time(quick_sort, arr_sorted))
    # Обратно отсортированные
    results['reversed']['selection'].append(measure_time(selection_sort, arr_reversed))
    results['reversed']['quick'].append(measure_time(quick_sort, arr_reversed))

for key in results:
    plt.figure()
    plt.plot(sizes, results[key]['selection'], label='Selection Sort')
    plt.plot(sizes, results[key]['quick'], label='Quick Sort')
    plt.xlabel('Размер списка')
    plt.ylabel('Время (сек)')
    plt.title(f'Время сортировки для {key} списка')
    plt.legend()
    plt.grid(True)
    plt.show()
