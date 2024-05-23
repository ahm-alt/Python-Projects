calc = input("Expression: ").strip()
x, m, y = calc.split(" ")
x = float(x)
y = float(y)

if m == "+":
    print(round(x + y, 1))
elif m == "-":
    print(round(x - y, 1))
elif m == "*":
    print(round(x * y, 1))
elif m == "/":
    print(round(x / y, 1))