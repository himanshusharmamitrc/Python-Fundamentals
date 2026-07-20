name = input("What is your name? ")
print("Welcome", name)
age = int(input("What is your age? "))
print("Your age is", age)
course = input("What is your course? ")
print("Your course is", course)
college = input("What is your college name? ")
print("Your college name is", college)
dream = input("What is your dream? ")
print("Your dream is", dream)

#using float
height = float(input("Enter your height?"))
print("Height", height)

#using str
name = str(input("Enter your name?"))
print("Your name is", name)

age = 18
print(str(age) + " is your age") #using str to convert int to str

#using if
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")

#using if else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#using if elif else
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:   
    print("Grade D")
else:
    print("Fail")

 


