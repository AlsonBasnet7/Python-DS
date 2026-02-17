# Step 1: Take input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


while num2 != 0:
    num1, num2 = num2, num1 % num2


# # Step 2: Repeat until remainder is 0
# while num2 != 0:
#     r = num1 % num2       # calculate remainder
#     num1 = num2           # replace num1 with num2
#     num2 = r              # replace num2 with remainder

# Step 3: Print the GCD
print("The GCD is:", num1)




# while num2 != 0:
#     num1, num2 = num2, num1 % num2
