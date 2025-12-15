import random

letters = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+']

nr_letter = int(input("How many letters do you want? \n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_number = int(input("How many numbers do you want? \n"))

# Hard password
password_list = []

for _ in range(nr_letter):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_number):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
