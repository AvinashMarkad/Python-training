def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Iterative Fibonacci({num}):", fibonacci_iterative(num))
    print(f"Recursive Fibonacci({num}):", fibonacci_recursive(num))
    print(f"Memoized Fibonacci({num}):", fibonacci_memoization(num))
