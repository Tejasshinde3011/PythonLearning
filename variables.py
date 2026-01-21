print('hello world')
for i in range(11):
    a=i*5
    print(a)

# --------VARIABLES, DATA TYPES, OPERATORS-------------

# Check if a number is even or odd using modulus (%).
a=int(input("Enter the number : "))
if a%2==0:
    print("The number is Even.")
else  :  
    print("The number is Odd.")


# average pf 2 numbers
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = (a+b)/2
print(f"The average is : {c}")


# Write a python program to find remainder when a number is divided by z.
a = int(input("Enter the number to be divided : "))
b = int(input("Enter the number with which the other number is divided : "))
print(f"The remainder is : {a%b}")

# Write a program that asks the user for two numbers and prints whether their sum is greater than 100.
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))

if a+b>100:
    print(f"The sum of {a} and {b} is Greater than 100")
else:    
    print(f"The sum of {a} and {b} is Greater than 100")

# ------STRING--------

name = input("Enter your name: ").strip()
print(f"Hello {name.title()}! Your name has {len(name)} letters.")

#Check for palindrome
text = input("Enter the string : ")
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# count vowels and consonants
text = input("Enter the string : ")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0
for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count +=1
        else:
            c_count +=1
print(v_count)       
print(c_count)       

#Find Frequency of Each Character
text = input("Enter the string : ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

text = input("Enter the string : ")
result = ""
for ch in text:
    if ch not in result:
     result +=ch    
print(result)

# Find the Longest Word in a Sentence
text = input("Enter the string : ")
list = text.split()
print(list)
result = max(list, key=len)
print(result)

# Replace Spaces with Underscores
text = input("Enter the string : ")
new_text = text.replace(" ","_")
cap = new_text.title()
print(new_text)
print(cap)

