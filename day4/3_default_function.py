def greet(name="himanshu"):  #function defination with default argument
    print("Good Day",name)

greet()
greet("nishant") #function call with default argument

#Two parameters with default argument
def add(a,b=5):
    print(a+b)

add(10)
add(10,20)   