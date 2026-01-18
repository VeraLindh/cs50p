answer = (
    input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    .lower()
    .strip()
    # for some reason, i had a bug here. i had to add .strip() and .lower()
    # inside this pair of parentheses to make it work.
)

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
