# issubset()
#example1

A = {10, 20}

B = {10, 20, 30, 40}

print(A.issubset(B))
print()

#example2
A = {10, 20, 50}

B = {10, 20, 30, 40}

print(A.issubset(B))
print()

# issuperset()
#example1
A = {10, 20, 30, 40}

B = {10, 20}

print(A.issuperset(B))
print()

#example2
A = {10, 20}

B = {10, 20, 30}

print(A.issuperset(B))
print()

# isdisjoint()
#example1
A = {10, 20}

B = {30, 40}

print(A.isdisjoint(B))
print()

#example
A = {10, 20}

B = {20, 30}

print(A.isdisjoint(B))
print()


#practice

A = {"Python", "Java"}

B = {"Python", "Java", "C++"}

C = {"HTML", "CSS"}

print(A.issubset(B))

print(B.issuperset(A))

print(A.isdisjoint(C))

print(B.isdisjoint(C))
