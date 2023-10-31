#print("Hello teacher")
#print("Homework №8 Banul")

#Написати валідації за допомогою регулярних виразів:
#1.  домашній номер телефону (тільки цифри та довжина номера)

import re
def valid_home_number(number):
    pattern = re.compile(r'^\d{10}$')
    return bool(pattern.match(number))

home_number = "1234567"
print(valid_home_number(home_number))