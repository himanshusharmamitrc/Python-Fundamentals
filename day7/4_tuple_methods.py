# Tuple Methods

numbers = (10, 20, 30, 10, 40, 10, 50)

print("Original Tuple:", numbers)

# count()
print("\ncount()")
print(numbers.count(10))
print(numbers.count(20))
print(numbers.count(100))

# index()
print("\nindex()")
print(numbers.index(10))
print(numbers.index(30))
print(numbers.index(40))
print(numbers.index(50))

# len()
print("\nlen()")
print(len(numbers))

# max()
print("\nmax()")
print(max(numbers))

# min()
print("\nmin()")
print(min(numbers))

# sum()
print("\nsum()")
print(sum(numbers))

# sorted()
print("\nsorted()")
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# tuple()
print("\ntuple()")
list1 = [1, 2, 3, 4, 5]
print(tuple(list1))

# any()
print("\nany()")
print(any(numbers))

# all()
print("\nall()")
print(all(numbers))