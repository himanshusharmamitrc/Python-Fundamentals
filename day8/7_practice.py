# Practice 1

student = {
    "name": "Himanshu Sharma",
    "age": 20,
    "branch": "AI-ML",
    "city": "Alwar"
}

print(student["name"])
print(student["branch"])


# Practice 2

student["semester"] = 5

print(student)


# Practice 3

student["age"] = 21

print(student)


# Practice 4

print(student.keys())
print(student.values())
print(student.items())


# Practice 5

print(student.get("city"))
print(student.get("email"))


# Practice 6

student.pop("city")

print(student)


# Practice 7

student_copy = student.copy()

print(student_copy)


# Practice 8

student_copy.clear()

print(student_copy)


# Practice 9

students = {

    "student1": {
        "name": "Himanshu",
        "branch": "AI-ML"
    },

    "student2": {
        "name": "Rahul",
        "branch": "CSE"
    }

}

print(students["student1"]["name"])
print(students["student2"]["branch"])