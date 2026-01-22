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

# Write a program to sort a list in ascending order without using sort().
arr6 = [2,5,9,345,7,2,4,46,9,78,34]
arr6 = list(set(arr6))
for i in range(len(arr6)):
    for j in range(i+1, len(arr6)):
        if arr6[i]>arr6[j]:
            arr6[i],arr6[j] = arr6[j],arr6[i]
print(arr6)

# Write a program to merge two lists into a single list.
arr7 = [2,5,9,345,7,2,4,46,9,78,34]
arr8 = [1,2,5,3,2,7,6,4,3,1]
arr_new = []
for i in arr7:
        arr_new.append(i)
for j in arr8:
    arr_new.append(j)
print(arr_new)
print("Method 2")
arr7.extend(arr8)
print(arr7)

# Write a program to count the frequency of each element in a list.
arr8 = [1,2,5,3,2,5,7,6,4,3,1,7,4,2]
freq = {}
for i in arr8:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
for i in freq:
    print(f"Frequency of {i} : {freq[i]} times")

arr = [1, 2, 2, 3, 1, 4, 2]

visited = [False] * len(arr)

for i in range(len(arr)):
    if visited[i]:
        continue

    count = 1
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            count += 1
            visited[j] = True

    print(arr[i], "->", count)










