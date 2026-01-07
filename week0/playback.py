# ask user for input, convert to str
statement = str(input("What do you got to say?\n"))

# replace spaces with three dots, if "space" replace with ...
statement = statement.replace(" ", "...")

# return sentence to user
print(statement)
