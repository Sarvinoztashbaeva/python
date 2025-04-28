name = input("Your name: ")
age = int(input("Your year of birth: "))
print(f"Your name: {name}")
print(f"You are {2025-age} years old")

txt = 'LMaasleitbtui'
print(txt[::2], txt[1::2])

txt = 'MsaatmiazD'
print(txt[::2])

txt = "I'am John. I am from London"
txt[21:]

smth = input("Write anything: ")
print(smth[::-1])

txt = "Hello, my name is Sarah"
vowels = "aeiouAEIOU"
vowels_count = sum(txt.count(vowel) for vowel in vowels)
print(f"There are {vowels_count} vowels")

user_input = input("Enter numbers separated by spaces: ")
numbers = [float(num) for num in user_input.split()]
max_value = max(numbers)
print("The maximum value is:", max_value)

name = input("Write any word")
if name[::] == name[::-1]:
 print("The word is palindrome.")
else:
 print("The word is not palindrome.")

email = input("Enter your email address: ")
parts = email.split("@")
if len(parts) == 2:
    domain = parts[1]
    print("The domain is:", domain)
else:
    print("Invalid email address.")

import random
import string


letters = string.ascii_letters  
digits = string.digits         
special_chars = string.punctuation  

all_chars = letters + digits + special_chars
password_length = 12
password = ''.join(random.choice(all_chars) for _ in range(password_length))
print("Generated password:", password)

