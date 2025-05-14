text = input("Enter a string: ")

print(f"Original string: {text}")
print(f"First 5 characters: {text[:5]}")
print(f"Last 5 characters: {text[-5:]}")
print(f"Middle part (index 2 to 6): {text[2:7]}")
print(f"Every second character: {text[::2]}")
print(f"Reversed string: {text[::-1]}")

text1 = "Hello"
new_text = 'Y' + text1[2:]
print(f"Original String: {text}")
print(f"Modified String: {new_text}")