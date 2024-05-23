camel = input("camelCase: ")

for i in camel:
    if i.isupper():
        n = "_" + i.lower()
        camel = camel.replace(i, n, 1)

print("snake_case:",camel)