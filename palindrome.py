# Palindrome Program

text = input("Enter a string: ")

# Convert to lowercase (optional)
text = text.lower()

if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
