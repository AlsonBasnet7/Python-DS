student={"name":"Alson","age":21}
print(student["name"])
student["city"]="Jhumka"
print(student)
print(student.keys())
print(student.values())
print(student.items())
#dictinary comprehensions:
squares={x:x**2 for x in range(5)}
print(squares)