# Reverse a string
str1 = "python"
print(str1[ : :-1])

# Check palindrome
str2 = "madam"
str3 = str2[::-1]
if str2 == str3:
    print("Yes it is a palindrome")
else:
    print("It is not a palindrome")

# Count vowels and consonants
str4 = "abiodf"
count_vowels = 0
count_consonants = 0
for ch in str4:
    if ch.isalpha():
        if ch in ["a", "e", "i", "o", "u", "A", "E", "I", "O","U"] :
         count_vowels+=1
        else :
         count_consonants+=1
    else:
       print("Input is invalid.")
print(count_consonants)
print(count_vowels)

# Count total characters (excluding spaces)
str5 = "This is a new string"
count=0
for ch in str5:
   if ch.isalpha():
      count+=1
print(f"the total number of characters are {count}")

# Replace all spaces with underscores
str6 = "Python is fun"
str7 = str6.replace(" ","_")
print(str7)

# Count frequency of each character
str8 = "This is a nice banana"
freq = {}
for ch in str8 :
    if ch in freq:
       freq[ch]+=1
    else:
       freq[ch]=1
print(freq)

# Remove duplicate characters
str9 = "programming"
charatcers = " "
for ch in str9:
   if ch not in charatcers:
      charatcers += ch
print(charatcers)

# Find the longest word
str10 = "This is the new biggest string"
words = str10.split()
longest = words[0]
for word in words:
   if len(word)>len(longest):
        longest = word

print("longest words : ", longest )

# Convert to title case (without using .title())
str11 = "i want to capitlise all the words in this sentence"
words = str11.split()
result = []
for word in words:
   result.append(word[0].upper() + word[1:])
final = " ".join(result)
print(final)


      
