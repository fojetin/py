import re
S = input()
print(len(re.findall(r'[a-zA-Z]+-[a-zA-Z]+|[a-zA-Z]+', S)))
