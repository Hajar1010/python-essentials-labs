text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

# Remove spaces and make everything lowercase
cleaned1 = text1.replace(" ", "").lower()
cleaned2 = text2.replace(" ", "").lower()

# Check if both are non-empty and contain the same letters
if cleaned1 != "" and cleaned2 != "" and sorted(cleaned1) == sorted(cleaned2):
    print("Anagrams")
else:
    print("Not anagrams")
