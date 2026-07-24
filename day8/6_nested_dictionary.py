# Nested Dictionary

students = {

    "student1": {
        "name": "Himanshu Sharma",
        "age": 20,
        "branch": "AI-ML"
    },

    "student2": {
        "name": "Rahul Kumar",
        "age": 21,
        "branch": "CSE"
    },

    "student3": {
        "name": "Aman Singh",
        "age": 22,
        "branch": "IT"
    }

}

print(students)

print("\nStudent 1")
print(students["student1"])

print("\nStudent 2 Name")
print(students["student2"]["name"])

print("\nStudent 3 Branch")
print(students["student3"]["branch"])