import json

file = open("passwords", 'r')
passwords = []

for line in file:
    passwords.append(line.rstrip())

file.close()

print(json.dumps(passwords))
