#use the extend() method to add multiple items to the end of the list.
fruits = ["apple", "banana", "cherry"]
fruits.extend(["orange", "kiwi", "mango"])
print(fruits)

#use extend() to add multiple numbers to the list.
numbers = [1, 2, 3, 4]  
numbers.extend([5,6,7])
print(numbers)

# use extend() to add one list to another list.
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)