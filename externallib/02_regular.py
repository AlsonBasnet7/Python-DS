#Regular expression or regex are powerful tools for patterns matching in strings. 
#regex is the built in regular expression in the python
import re
text= "Hey, My name is Morse and I am learning Python along with Data Science."
print("Old Text:",text)

match = re.search("Python", text)
if match:
    print("Match found!")
    print("Start index:", match.start())
    print("End index:", match.end())

# Find all occurrences of a pattern
matches = re.findall("I", text, re.IGNORECASE)  # Case-insensitive search
print("Matches:", matches)

# Replace all occurrences of a pattern
new_text = re.sub("Morse", "Alson", text)
print("New text:", new_text)

#Compile a regrex for efficieny (if used multiple time)
pattern = re.compile(r"\b\w+\b")  # Matches whole words
words = pattern.findall(text)
print("Words:", words)