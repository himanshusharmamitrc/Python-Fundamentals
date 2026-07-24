# union()

set1 = {10, 20, 30}
set2 = {30, 40, 50}

result = set1.union(set2)

print(result)
print()

# intersection()

set1 = {10, 20, 30}
set2 = {30, 40, 50}

result = set1.intersection(set2)

print(result)
print()


# difference()

set1 = {10, 20, 30}
set2 = {30, 40, 50}

result = set1.difference(set2)

print(result)
print()


# symmetric_difference()

set1 = {10, 20, 30}
set2 = {30, 40, 50}

result = set1.symmetric_difference(set2)

print(result)
print()


# practice
A = {"Python", "Java", "C++"}
B = {"Java", "JavaScript", "Python"}

print("Union :", A.union(B))

print("Intersection :", A.intersection(B))

print("Difference :", A.difference(B))

print("Symmetric Difference :", A.symmetric_difference(B))
