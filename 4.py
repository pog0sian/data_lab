import time
from matplotlib import pyplot as plt

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def fib_with_lucas(n):
    if n == 0 or n == 1:
        return n
    i = n // 2
    j = n - i
    return (lucas(i) + fibonacci(j) * fibonacci(i) + lucas(j)) // 2

def lucas_with_fib(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return fib_with_lucas(n - 1) + fib_with_lucas(n + 1)

N = 30
fib_times = []
fib_lucas_times = []

start_fib = time.time()
fibonacci_result = fibonacci(N)
end_fib = time.time()
fib_time = end_fib - start_fib

start_lucas = time.time()
lucas_result = lucas(N)
end_lucas = time.time()
lucas_time = end_lucas - start_lucas

print(f"Время вычисления F({N}): {fib_time:.4f} секунд")
print(f"Время вычисления L({N}): {lucas_time:.4f} секунд")

N_values = list(range(1, 30))

for N in N_values:
    start = time.time()
    fibonacci(N)
    fib_times.append(time.time() - start)

    start = time.time()
    fib_with_lucas(N)
    fib_lucas_times.append(time.time() - start)

plt.plot(N_values, fib_times, label='fibonacci')
plt.plot(N_values, fib_lucas_times, label='fib_with_lucas')
plt.xlabel('n')
plt.ylabel('Время (сек)')
plt.legend()
plt.title('Сравнение быстродействия')
plt.show()