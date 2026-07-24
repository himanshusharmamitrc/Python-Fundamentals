# Dictionary Methods

student = {
    "name": "Himanshu Sharma",
    "age": 20,
    "branch": "AI-ML",
    "college": "MITRC Alwar",
    "city": "Alwar"
}

print("Original Dictionary")
print(student)

# keys()
print("\nkeys()")
print(student.keys())

# values()
print("\nvalues()")
print(student.values())

# items()
print("\nitems()")
print(student.items())

# get()
print("\nget()")
print(student.get("name"))
print(student.get("college"))
print(student.get("email"))   # Key doesn't exist

# update()
print("\nupdate()")

student.update({
    "age": 21,
    "semester": 5,
    "city": "Jaipur"
})

print(student)

# copy()
print("\ncopy()")

student_copy = student.copy()

print(student_copy)

# clear()
print("\nclear()")

student_copy.clear()

print(student_copy)