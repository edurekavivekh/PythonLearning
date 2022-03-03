#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pydata Generator!")
nr_letters= int(input("How many letters would you like in your data?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_pickup = []
symbols_pickup = []
numbers_pickup = []

#Pickup random letters from letters list
for i in range(0,int(nr_letters)):
  rnd_letter_index = random.randint(0,len(letters) - 1)
  letters_pickup.append(letters[rnd_letter_index])

#Pickup random symbols from symbols list
for j in range(0,int(nr_symbols)):
  rnd_symbols_index = random.randint(0,len(symbols) - 1)
  symbols_pickup.append(symbols[rnd_symbols_index])

#Pickup random numbers from numbers list
for k in range(0,int(nr_numbers)):
  rnd_numbers_index = random.randint(0,len(numbers) - 1)
  numbers_pickup.append(numbers[rnd_numbers_index])

data = []

#Create combined list of numbers, symbols and letters
for l in letters_pickup:
  data.append(l)
for m in symbols_pickup:
  data.append(m)
for n in numbers_pickup:
  data.append(n)


random.shuffle(data)
password = ""
for i in data:
    password = password + i

print(f'Your password is: {password}')
