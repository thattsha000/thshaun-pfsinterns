import pyperclip
import random
import string

print("This code is meant for developing a suitable password. To obtain the randomly generated password, input in the desired type of characters. ")
print("Use D for digits, S for special characters, U for uppercase characters, and L for lowercase characters.  ")
print("Example: Inputting DSUL would include a password with all of these characters while inputting DUL would include Digits, Uppercase, and Lowercase characters.")
char_set  = list(input("Input the types of characters that you would like in your password: "))
length = int(input("Choose the length of the password: "))

available_chars = []
if "D" in char_set:
    available_chars += string.digits
if "L" in char_set: 
    available_chars += string.ascii_lowercase
if "S" in char_set:
    available_chars += string.punctuation
if "U" in char_set: 
    available_chars += string.ascii_uppercase

def get_password(len, chars):
    return "".join([random.choice(chars) for x in range(len)])

password = get_password(length,available_chars)
print(f"Here is your randomly generated password: {password}")
print()
copy_options = input("Would you like to copy your password(y/n): ")
if copy_options == 'y': 
    pyperclip.copy(password)
    print("Your password has been copied to your clipboard!")


