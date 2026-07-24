# Set

numbers = {10, 20, 30, 40}

print(numbers)

# Add

numbers.add(50)

print(numbers)

# Update

numbers.update({60, 70})

print(numbers)

# Remove

numbers.remove(20)

print(numbers)

# Discard

numbers.discard(100)

print(numbers)

# Pop

removed = numbers.pop()

print("Removed:", removed)

print(numbers)

# Union

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))

# Intersection

print(A.intersection(B))

# Difference

print(A.difference(B))

# Symmetric Difference

print(A.symmetric_difference(B))

# Subset

X = {10, 20}
Y = {10, 20, 30, 40}

print(X.issubset(Y))

# Superset

print(Y.issuperset(X))

# Disjoint

C = {100, 200}

print(X.isdisjoint(C))

# Clear

C.clear()

print(C)