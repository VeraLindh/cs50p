# ask user for input (x y z)
expression = input("Expression: ")

# split the input into parts
x, y, z = expression.split(" ")

# convert x and z to float
x = float(x)
z = float(z)

# perform the operation based on y
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    print("Unknown operator")
