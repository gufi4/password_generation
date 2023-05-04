from random import choice

digits = '0123456789'
lowercase_letters_en = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
uppercase_letters_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

pwd_length = int(input('Enter password length: '))
pwd_digits = input('Include numbers (yes = y, no = n): ')
pwd_uppercase_en = input('Include uppercase letters en (yes = y, no = n): ')
pwd_lowercase_en = input('Include lowercase letters en (yes = y, no = n): ')
pwd_uppercase_ru = input('Include uppercase letters ru (yes = y, no = n): ')
pwd_lowercase_ru = input('Include lowercase letters ru (yes = y, no = n): ')
pwd_punctuation = input('Include symbols "!#$%&*+-=?@^_"? (yes = y, no = n): ')

if pwd_digits == 'y':
    chars += digits
if pwd_uppercase_en == 'y':
    chars += uppercase_letters_en
if pwd_lowercase_en == 'y':
    chars += lowercase_letters_en
if pwd_uppercase_ru == 'y':
    chars += uppercase_letters_ru
if pwd_lowercase_ru == 'y':
    chars += lowercase_letters_ru
if pwd_punctuation == 'y':
    chars += punctuation

password = ''

for i in range(pwd_length):
    password += choice(chars)

print('\n', password, '\n', sep='')

