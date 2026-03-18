numbers = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

# Ascending sort
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print("Ascending:", numbers)

# Descending sort
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print("Descending:", numbers)