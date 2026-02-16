# String Manipulation Challenges
# Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
# Find the index of the word "Python" in sentence.
# Convert the entire sentence to uppercase and print it.

sentence="Coding in Python is fun"
sentences=sentence.replace("fun","awesome")
print("The given sentence =",sentence)
print("The update sentence = ", sentences)
findIndex=sentences.index("Python")
print("The index of the python is ", findIndex)
upperCase=sentences.upper()
print("The Upper Case of the Sentencs is",upperCase)