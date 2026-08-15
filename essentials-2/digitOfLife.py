date = input("Enter your birthday (YYYYMMDD): ")

while len(date) != 8 or not date.isdigit():
    date = input("Enter your birthday (YYYYMMDD): ")

total = sum(int(digit) for digit in date)

while total >= 10:
    total = sum(int(digit) for digit in str(total))

print(total)
