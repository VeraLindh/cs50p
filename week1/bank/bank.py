# ask for greeting
greeting = input("Greeting: How are you doing? ").strip().lower()

# if greeting starts with "hello", output $0
if greeting.startswith("hello"):  # i didn't know there was such thing as startswith!!!!
    print("$0")
# if greeting starts with "h" (but not "hello"), output $20
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
