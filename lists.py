# They are indexed
# They allow duplicates
# They can contain any type of data
people = ["John", "Mary", "Mary", "Peter", "Paul", 60, 5.5, True]

# print(people)
# print(people[1])
# print(len(people))

# index = len(people) - 1
# print(index)
# print(people[-1])
# print(people[index])

# # Range
# print(people[1:4])
# print(people[1:])
# print(people[:4])
# print(people[:-3])

# # Reassigning
# people[1] = "Kevin"
# print(people)

# Inserting
people.insert(1, "Lisa")
print(people)

# Removing
people.remove("Mary")
print(people)

# Appending
people.append("John")
print(people)
