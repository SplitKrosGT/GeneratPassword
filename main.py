import random

# Набор доступных символов.
ARRAY_SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'r', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 '!', '@', '#', '$', '%', '&', '*', '?', '/', '.', ',', '\\', ';', ':', '|']

# Получаем количесмтво символов в пароле.
CONST_COUNT_SYMBOLS = 4
custom_count_symbols = int(input('ведите количество символов в пароле:'))
if custom_count_symbols > 0:
    count_symbols = custom_count_symbols
else:
    count_symbols = CONST_COUNT_SYMBOLS


count_variant = (len(ARRAY_SYMBOLS) ** count_symbols)

# Функция случайных символов.
def random_symbols():
    return ARRAY_SYMBOLS[
        random.randint(0, len(ARRAY_SYMBOLS) - 1)
    ]

print(f'Приложение версии 0.0.1')
print(f'Количество доступных символов: {len(ARRAY_SYMBOLS)}')
print(f'Количество возможных вариантов: {count_variant}')

# Массив символов
password_array = [i for i in range(0, count_symbols)]

password = ''

for i in password_array:
    password = password + f'{random_symbols()}'

print(f'ваш подобраный пароль: {password}')

# Запись пароля в файл.
with open('password.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))
