# #sum of n number of digits.
# def sum(n):
#     return n+n
# number=int(input("Enter the numbers"))
# print("The sum of the n number of digits is",sum(number))

def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        num = int(input(f"Enter a number: "))
        return num + sum_of_numbers(n-1)

n = int(input("How many numbers do you want to add? "))
print("The sum of the numbers is", sum_of_numbers(n))
