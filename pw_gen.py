import random
import string

length = int(input("How long your password should be\n"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

all_characters = (lower + upper + digits + special_characters)

list_password = random.sample(all_characters, length)
complete_password = "".join(list_password)

print(complete_password)