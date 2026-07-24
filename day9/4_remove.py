# remove()

numbers = {10, 20, 30, 40}

print("Before Remove")
print(numbers)

numbers.remove(20)

print("After Remove")
print(numbers)
print()

# discard()

numbers = {10, 20, 30, 40}

numbers.discard(20)

print(numbers)
print()


# pop()

numbers = {10, 20, 30, 40}

removed_value = numbers.pop()

print("Removed:", removed_value)
print(numbers)
print()

# clear()

numbers = {10, 20, 30, 40}

numbers.clear()

print(numbers)
print()


# practice

fruits = {"Apple", "Banana", "Mango", "Orange"}

fruits.remove("Banana")

fruits.discard("Grapes")

print(fruits)

removed = fruits.pop()

print("Removed:", removed)

print(fruits)

fruits.clear()

print(fruits)