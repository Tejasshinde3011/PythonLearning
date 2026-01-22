# Create and access
tup = (1,2,3,4)
print(tup[0])
print(tup[3])

# Write a program to find the length of a tuple.
tup = (1,2,3,4,5)
print(len(tup))
print(3 in tup)
print(3 not in tup)

# Write a program to count how many times an element appears in a tuple.
tup = (1,3,2,4,5,643,2,46,4,2,5,35,1)
freq = {}
for i in tup:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i]+=1
for i in freq:
    print(f"frequency of {i} : {freq[i]} times")

# Write a program to find the index of a given element in a tuple.
tup = (1,3,2,4,5,643,46,5,35)
# element = int(input("Enter the element to find index : "))
# if element in tup:
#     print(f"Index : {tup.index(element)}")
# else:
#     print("Element not present in tuple.")

# Write a program to convert a tuple into a list, modify it, and convert it back to a tuple.
tup = (1,3,2,4,5,643,46,5,35)
lis1 = list(tup)
print(lis1)
tup1 = tuple(lis1)
print(tup1)

# Write a program to find the maximum and minimum elements in a tuple.
tup = (1,3,2,4,5,643,46,5,35)
largest = float('-inf')
smallest = float('inf')
for i in tup:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print(f"Largest element is : {largest}")
print(f"smallest element is : {smallest}")

# Write a program to reverse a tuple.
tup = (1,3,2,4,5,643,46,5,35)
reverse = ()
for i in range(len(tup) -1,-1,-1):
    reverse = reverse + (tup[i],)
print(reverse)

# Given a tuple (10, 20, 30), unpack it into three variables and print them.
tup = (10,20,30)
a,b,c = tup
print(f"a= {a}, b= {b}, c={c}")

# Given a nested tuple ((1,2),(3,4)), print element 4.
tup = ((1,2), (3,4))
print(tup[1][1])

# Given a nested tuple ((1,2),(3,4)), print all elements with separate variables.
tup = ((1,2), (3,4))
(a,b), (c, d) = tup 
print(f"{a}, {b}, {c}, {d}")

# Write a program to remove a random element from a tuple.
tup = (1,3,2,4,5,643,46,5,35)
list1 = list(tup)
list1.remove(list1[1])
print(list1)
import random
indx = random.randrange(len(list1))
remove_element = list1.pop(indx)
new_tup = tuple(list1)
print(new_tup)

# Write a program to use a tuple as a key in a dictionary.
location = (10,20)
data = {}
data[location] = "Point A"
print(data)
