# Remove Elements

student = {
    "name": "Himanshu",
    "age": 20,
    "branch": "AI-ML",
    "city": "Alwar"
}

print(student)

# pop()

student.pop("age")

print(student)

# popitem()

student.popitem()

print(student)

# del

del student["branch"]

print(student)

# clear()

student.clear()

print(student)

print()

#example 2

student = {
    "name":"Rahul",
    "age":19,
    "branch":"CSE",
    "city":"Jaipur"
}

student.pop("city")

print(student)

student.popitem()

print(student)

del student["age"]

print(student)

student.clear()

print(student)
