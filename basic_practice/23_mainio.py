# import operation
# student=operation.read("text.txt")
# print(student)
# operation.add(student,"ID004","Rushan",69)
# print(student)

import operation

student = operation.read("text.txt")
print(student)

student = operation.add(student, "ID004", "Rushan", 69)
print(student)

operation.update(student)
operation.write("text.txt",student)
print(student)


