# Take input of numbers separated by spaces
numbers = input("Enter numbers separated by space: ").split()

# Convert each input into integer
numbers = [int(num) for num in numbers]

# Function to reverse a number
def reverse_number(n):
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

# Reverse each number in the list
reversed_list = [reverse_number(num) for num in numbers]

print("Original list:", numbers)
print("Reversed numbers list:", reversed_list)