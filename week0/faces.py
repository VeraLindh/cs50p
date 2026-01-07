def convert(n):
    n = n.replace(":)", "🙂").replace(":(", "🙁")
    return n

def main():
    phrase = input("Enter your phrase: ").strip()
    message = convert(phrase)
    print(message)

main()

## notes
# thought this would be way too complicated
# just needed to replace the unicode emojis
# with their emoji counterparts
