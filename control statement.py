# Write a program to check whether a number is positive, negative, or zero.
num = -345
if num >0:
    print("It is a positive integer")
elif num <0:
    print("It is a negative integer")
else:
    print("It is 0")

# arrange in ascending order and find the largest number from them.
a= "34"
b= "345"
c= "532"

array = [a,b,c]
largest = array[0]
for i in array:
   if i> largest:
      largest = i
for k in range(len(array)):
   for j in range(k+1, len(array)):
      if array[k]>array[j]:
         array[k], array[j] = array[j], array[k]
print(array)
print(f"The largest number is {largest}")

# Write a program to print grade based on marks:
marks = 89
if marks>=90:
   print("Grade A")
elif marks>=75:
   print("Grade B")
elif marks>=60:
   print("Grade C")
else:
   print("Fail")

# Write a program to print the number of days in a month based on month number.
month = 4
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:
    print("Invalid month number")

# Write a program that performs + − × ÷ based on user choice.
i = 6
j = 8
print("1,add")
print("2,sub")
print("3,mul")
print("4,div")
operation = 3
if operation == 1:
   print(f"Result is : {i+j}")
elif operation == 2:
   print(f"Result is : {i-j}")
elif operation == 3:
   print(f"Result is : {i*j}")
else:
   print(f"Result is : {i/j}")

# Sum of First n Numbers
sum=0
for i in range(20):
   sum+=i
print(sum)

# Write a program to print the multiplication table of a given number.
num = 20
for i in range(1,11):
   print(f"{num} X {i} = {num*i}")

# Write a program to calculate the factorial of a number.
number = 5
factorial = 1
for i in range(1, number+1):
   factorial = factorial * i
print(factorial)

# Write a program to count the number of digits in a number.
num1 = 1234567
count=0
if num1 == 0:
   count =1
else:
   while num1!=0:
      count+=1
      num1 = num1//10
print(count)

# Write a program to check whether a given number is a prime number.
num = 3
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# Write a program to reverse a given number.
num = 2345
rev=0
while num!=0:
   digit = num%10
   print(digit)
   rev = rev * 10 + digit
   num = num//10
print(rev)

# Write a program to calculate the sum of digits of a given number.
num = 2345
while num!=0:
   digit = num%10
   num =num//10
   sum = sum + digit
print(sum)

# Write a program to print the first n terms of the Fibonacci series.
num = int(input("Enter a number: "))
a, b = 0, 1
if num<=0:
   print("Give positive number")
elif num==1:
   print(a)
else:
   print(a, b, end=" ")
   for i in range(2,num):
      c = a+b
      print(c, end=" ")
      a=b
      b=c
