import random as random
import string as string

no_letters = int(letters)
no_symbols = int(symbols)
no_numbers = int(numbers)


letters = string.ascii_letters
numbers = string.digits
symbols = "!#$%&()*+"
random_letters = random.choices(letters, k=no_letters)
random_symbols = random.choices(symbols, k=no_symbols)
random_num = random.choices(numbers, k=no_numbers)

temp = "".join(random_letters + random_symbols + random_num)
random_password = "".join(random.sample(temp, len(temp)))

print(f"Your extreme random password is: {random_password}")
print(f"Length of password: {len(random_password)}")
