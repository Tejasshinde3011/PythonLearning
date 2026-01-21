# Sum of elements
arr1 = [1,2,3,4,5,6,7]
print(sum(arr1))
# Largest element, Smallest element
print(max(arr1))
print(min(arr1))
# Write a program to reverse a list with using built-in methods.
arr1.reverse()
print(arr1)

# Write a program to count the number of even and odd elements in a list.
arr2 = [2,5,9,345,7,2,4,46,9,78,34]
count_even=0
count_odd=0
for i in arr2:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(count_odd)
print(count_even)

# Write a program to reverse a list without using built-in methods.
arr3 = [2,5,9,345,7,2,4,46,9,78,34]
rev=[]
for i in range(len(arr3) -1,-1,-1):
    rev.append(arr3[i])
print(rev)

# Write a program to remove duplicate elements from a list.
arr4 = [1,2,5,3,2,7,6,4,3,1]
arr_new = []
for i in (arr4):
    if i not in arr_new:
        arr_new.append(i)
print(arr_new)

# Write a program to find the second largest element in a list.
arr5 = [2,5,9,345,7,2,4,46,9,78,34]
largest = second_largest = float('-inf')
for num in arr5:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)

arr5 = list(set(arr5)) #removes duplicate.
arr5.sort()
print(arr5[-2])









