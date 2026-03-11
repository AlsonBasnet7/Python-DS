# write a program that creates and oritns out a list containing only the unique elements from an existing list.
numbers = [1, 2, 3, 2, 4, 5, 3, 1]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)