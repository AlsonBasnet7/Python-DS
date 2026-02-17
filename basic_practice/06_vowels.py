text=input("Enter a string")
text=text.lower()
count =0
for char in text:
    if char in "aeiou":
        count+=1
print("The number of vowel letters are",count)