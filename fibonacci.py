# Slow- O(2^n) time
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Faster (Memoization)- O(n) time
memo = {0: 0, 1: 1}
def fibonacci_faster(n):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_faster(n - 1) + fibonacci_faster(n-2)
    return memo[n]
    