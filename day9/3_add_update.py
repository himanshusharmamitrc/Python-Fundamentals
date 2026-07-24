# add()

numbers = {10, 20, 30}

print("Before Add")
print(numbers)

numbers.add(40)

print("After Add")
print(numbers)
print()

# Duplicate Value

numbers = {10, 20, 30}

numbers.add(20)

print(numbers)
print()

# update() using Set

numbers = {10, 20, 30}

numbers.update({40, 50, 60})

print(numbers)
print()

# update() using List

numbers = {10,20,30}

numbers.update([40,50])

print(numbers)
print()

# update() using Tuple

numbers = {10,20,30}

numbers.update((40,50))

print(numbers)
print()
