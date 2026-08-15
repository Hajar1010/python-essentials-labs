text = input("Enter your message: ")

while True:
    try:
        shift = int(input("Enter the shift value (1-25): "))
        if 1 <= shift <= 25:
            break
    except ValueError:
        pass

encrypted = ""

for char in text:
    if char.islower():
        encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        encrypted += char

print(encrypted)
