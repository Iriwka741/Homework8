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

#def valid_mobil_number(number):
#    pattern = re.compile(r"^\+380\(\d{2}\)\d{3}-?\d{2}-?\d{2}$")
#    return bool(pattern.match(number))

#mobil_number = "+380(12)345-67-65"
#print(valid_mobil_number(mobil_number))
##################################################
#3. email (наявність @, домену: gmail.com наприклад,
#мінімальна довжина та максимальна на ваш вибір)

#def valid_email(email):
#    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$')
#    return bool(pattern.match(email))

#email = "homework8@gmail.com"
#print(valid_email(email))

########################################################
#4.ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

def valid_full_name(name):
    pattern = re.compile(r'^[A-Za-zА-Яа-я]{2,20}\s[A-Za-zА-Яа-я]{2,20}\s[A-Za-zА-Яа-я]{2,20}$')
    return bool(pattern.match(name))

full_name = "Петренко Петро Петрович"
print(valid_full_name(full_name))