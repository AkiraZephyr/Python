student = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A'
}
print(student)

print(student['grade'])

text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)

person = {
    "name": "Bob",
    "location": {"city": "Paris", "country": "France"},
    "skills": ["Python", "Data Analysis"]
}
print(person)

def add(x,y): return x + y
def subtract(x,y): return x - y
operations = {
    "add": add,
    "subtract": subtract
}
print(operations["add"](10, 5))
print(operations["subtract"](10, 5))

config = {
    "theme": "dark",
    "autosave": True,
    "timeout": 300
}
print(config)
employee = {
    "id": 101,
    "name": "John",
    "department": "HR",
}
print(employee)