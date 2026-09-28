s1="Hello5world3Python2"
digits = []

for character in s1:
    if character.isdigit():
        digits.append(int(character))

total = sum(digits)
average = total / len(digits)

print("Sum", total)
print("Average:", average)