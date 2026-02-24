import random
import string

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers?\n"))

# 1. Define character pools using the string library
letters = string.ascii_letters
numbers = string.digits
symbols = "!#$%&()*+"
random_letters = random.choices(letters,k=nr_letters)
random_symbols =random.choices(symbols,k=nr_symbols)
random_num = random.choices(numbers,k=nr_numbers)

random_password ="".join(random_letters+random_symbols+random_num)
print(f"Your random password is: {random_password}")

print(f"Your extreme random password is: {"".join(random.sample(random_password, len(random_password)))}")


