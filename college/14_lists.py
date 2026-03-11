# write a program creates and prints a new with the elements of an existing list in the reverse order

num = int(input("Enter a number: "))

reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)