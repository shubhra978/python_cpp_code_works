# Create a string made of the first, middle, and last character
user_input= input("Enter string: \n" )
user_input_new=input("Enter string: \n" )

str_length=len(user_input)
str_mid=(str_length//2)

#string made of the first, middle, and last character
print(user_input[0],user_input[str_mid],user_input[str_length-1])

#string made of the middle three characters
for i in range(str_mid, str_mid+3):
    print(user_input[i], end="")
    
#Append new string in the middle of a given string
print(user_input[str_mid]+" "+user_input_new)

#Split a string on hyphens
user_input_split=user_input_new.split("-")
print(user_input_split)

#Find all occurrences of a substring in a given string by ignoring the case
print(user_input.count("hello"))

#Prefix/Suffix Check
print(user_input.startswith("hello"))
print(user_input.endswith("myname"))

# remove  white spaces
print(user_input.replace(" ",""))

#Vowel Counter
vowels = ["a","e","i","o","u"]
count=0
for vowel in vowels:
    for ch in user_input:
        if vowel == ch:
            count+=1

print(count)


#palindrome
def isPalindrome(phrase):
  phrase=phrase.replace(" ","")
  phrase=phrase.replace(".","")
  phrase=phrase.replace("!","")
  phrase = phrase.lower()
  phrase=list(phrase)
  reverse_phrase = phrase[::-1]
  if(phrase == reverse_phrase):
    return True
    
  return False
