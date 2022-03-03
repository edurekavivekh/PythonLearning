#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_selected = []
symbols_selected = []
numbers_selected = []
for i in range(0,int(nr_letters)):
  random_letter = random.randint(0,len(letters) - 1)
  letters_selected.append(letters[random_letter])
for j in range(0,int(nr_symbols)):
  random_symbols = random.randint(0,len(symbols) - 1)
  symbols_selected.append(symbols[random_symbols])
for k in range(0,int(nr_numbers)):
  random_numbers = random.randint(0,len(numbers) - 1)
  numbers_selected.append(numbers[random_numbers])
password = []
for l in letters_selected:
  password.append(l)
for m in symbols_selected:
  password.append(m)
for n in numbers_selected:
  password.append(n)

random.shuffle(password)
items = ""
for i in password:
    items = items + i
print(f'Your password is: {items}')


