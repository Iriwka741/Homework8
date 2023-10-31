#print("Hello teacher")
#print("Homework №8 Banul")

#Написати валідації за допомогою регулярних виразів:
#1.  домашній номер телефону (тільки цифри та довжина номера)

import re
#def valid_home_number(number):
#    pattern = re.compile(r'^\d{10}$')
#    return bool(pattern.match(number))

#home_number = "1234567"
#print(valid_home_number(home_number))

###############################################
#2. Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

def valid_mobil_number(number):
    pattern = re.compile(r"^\+380\(\d{2}\)\d{3}-?\d{2}-?\d{2}$")
    return bool(pattern.match(number))

mobil_number = "+380(12)345-67-65"
print(valid_mobil_number(mobil_number))