import requests
r= requests.get('https://api.github.com/users/AlsonBasnet7')
with open("codewithalson","w") as f:
    f.write(r.text)
print("Data is saved successfully")