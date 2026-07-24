# Packing

student = ("Himanshu", 20, "AI-ML")

print(student)


# Packing Without Parentheses

student = "Himanshu", 20, "AI-ML"

print(student)


# Unpacking

student = ("Himanshu", 20, "AI-ML")

name, age, branch = student

print(name)
print(age)
print(branch)


# Another Example

point = (10, 20)

x, y = point

print(x)
print(y)


# Using *

numbers = (10, 20, 30, 40, 50)

a, *b = numbers

print(a)
print(b)


# Using *

numbers = (10, 20, 30, 40, 50)

*a, b = numbers

print(a)
print(b)


# Using *

numbers = (10, 20, 30, 40, 50)

a, *b, c = numbers

print(a)
print(b)
print(c)


# Swapping

a = 10
b = 20

a, b = b, a

print(a)
print(b)


# Ignore Value

student = ("Himanshu", 20, "AI-ML")

name, _, branch = student

print(name)
print(branch)


# Nested Unpacking

student = ("Himanshu", (20, "AI-ML"))

name, (age, branch) = student

print(name)
print(age)
print(branch)