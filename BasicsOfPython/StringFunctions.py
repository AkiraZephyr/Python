text = "i'm philip."
print(f"Original String : {text}")

#convert to lowercase
print(f"Lowercase : {text.lower()}")

#convert to uppercasr
print(f"Uppercase : {text.upper()}")

#Capitalize the first letter
print(f"Capitalize : {text.capitalize()}")

#Title
print(f"Title : {text.title()}")

#Swap Case
print(f"Swap Case : {text.swapcase()}")

#Strip
print(f"Strip : {text.strip()}")

#Startswith
print(f"StartsWith philip: {text.startswith("philip")}")

#EndsWith
print(f"EndsWith philip: {text.endswith("philip")}")

#Find
print(f"Find : {text.find("philip")}")

#replace
print(f"Replace : {text.replace("philip", "sibi")}")

#count
print(f"Count : {text.count('p')}")

#split
print(f"Split : {text.split(" ")}")

#join
print(f"Join : {text.join("Hi")}")