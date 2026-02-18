# Recursion in Python
# Write a recursive function factorial(n) that returns the factorial of a number.
# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number
def fact(n):
    if n==1:
        return 1
    else:
     return n*fact(n-1)
num=int(input("Enter the number who's factorial you want to calculate"))

print("the factorial of the number is",fact(num))
