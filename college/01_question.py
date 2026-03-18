n = int(input("Enter how many numbers: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum + num

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)