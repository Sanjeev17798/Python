n = input("Enter a string: ")

alphabets = ''.join(char for char in n if char.isalpha())

print("Alphabets:", alphabets)
