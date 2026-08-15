text = input("Enter text: ")

# Remove spaces and make everything lowercase
cleaned = text.replace(" ", "").lower()

# Check if the text is not empty and is the same forwards and backwards
if cleaned != "" and cleaned == cleaned[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
