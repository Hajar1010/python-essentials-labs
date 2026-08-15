word = input("Enter the word: ").lower()
text = input("Enter the text: ").lower()

position = 0
found = True

for char in word:
    position = text.find(char, position)

    if position == -1:
        found = False
        break

    position += 1

if found:
    print("Yes")
else:
    print("No")
