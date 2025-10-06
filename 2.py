
def tribonacci(n):
    if n == 0 or n == 1:
        return 0 # Базовые случай
    elif n == 2:
        return 1 # Базовые случай
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3) # Рекурсивный случай

print(tribonacci(3))
