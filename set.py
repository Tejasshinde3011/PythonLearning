# Write a program to remove duplicate elements from a list using a set.
s1 = {1,2,3,4,5,3,2,68,2,4,6,2,4}
unique_set = set(s1)
print(unique_set)

# Create a set and add five elements to it.
new_set = set()
new_set.update([1,2,3,4,5])
print(new_set)

# Write a program to check whether an element exists in a set.
s1 = {1, 2, 3, 4, 5, 68, }
x = 2
if x in s1:
     print("Element exist in set")
else :
     print("Element not found")

# Given a list, count the number of unique elements using a set.
list1 = [1,2,3,4,6,4,2,4,6,8,4,3,6,9,75,3,2,5,7,8,7,5]
s2 = set(list1)
print("Unique elements are : ",s2 , " No. of unique elements is : ", len(s2))
list2 = list(s2)
print(list2)

# Write a program to find the union of two sets. Write a program to find the intersection of two sets. 
# Write a program to find the difference between two sets. Write a program to find the symmetric difference between two sets.
set_a = {1,2,3,4,5}
set_b = {3,4,5,6,7,8,9}
print("Union of two sets : ", set_a|set_b)
print("Intersection of two sets : ", set_a&set_b)
print("Difference of two sets : ", set_a-set_b)
print("Symmetric difference btw two sets : ", set_a^set_b)

# Write a program to check whether one set is a subset of another.
print(set_a.issubset(set_b))
set_c = {1,2,3}
set_d = {1,2,3,4,5,6,7,8,9}
print(set_c.issubset(set_d))

# Write a program to remove an element from a set using: remove(), discard()
s1 = {3,4,5,6,7,8,9}
s1.remove(6)
print(s1)
s1.discard(4)
print(s1)
# s1.remove(34)
# print(s1)

# Write a program to create a set of squares of even numbers using set comprehension.
squares_set = {x**2 for x in range(1,11)}
print(squares_set)


