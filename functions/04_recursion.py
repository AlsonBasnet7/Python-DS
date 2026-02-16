def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120
# most use case
# Must have a base case to avoid infinite recursion.
# Used in algorithms like Fibonacci, Tree Traversals.
