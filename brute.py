import hashlib
import os
import time
from Password import Password

password = Password()

count_symbols = input('ведите количество символов в пароле:')
pin_code = input("Введите PIN CODE для шифрования пароля (4 цифры): ")

if not pin_code.isdigit():
    pin_code = None

if count_symbols.isdigit():
    password.generation(int(count_symbols), pin_code)
else:
    password.generation(None, None)

print(password.password)
print(password.check_summa)

password_array = [0 for i in range(0, password.count_symbols)]

def next_array(array):
    array_count = [i for i in range(0, len(array))]
    c_symbols = len(password.ARRAY_SYMBOLS)
    if c_symbols == 0:
        return None

    else:
        if array[0] == c_symbols - 1:
            array[0] = 0
            plus = True

            if len(array) > 1:
                for i in array_count:
                    if i > 0:
                        if plus:
                            if array[i] < c_symbols - 1:
                                array[i] = array[i] + 1
                                break

                            elif array[i] == c_symbols - 1:
                                array[i] = 0
                            if i == len(array) - 1:
                                array.append(0)
                                break

            else:
                array.append(0)
        elif array[0] < c_symbols -1:
            array[0] = array[0] + 1

    return array

print(len((password.ARRAY_SYMBOLS)))
print(next_array(password_array))

start_time = time.time()
count_variant = 0

while True:
    count_variant += 1
    password_array = next_array(password_array)
    print(password_array)
    password_string = password.get_symbols(password_array)
    check_summa = hashlib.sha512(f'{password}{password.pin_code}'.encode()).hexdigest()
    print(password_string)

    print(check_summa)

    if check_summa == password.check_summa:
        print(f'Совпадение: {password_string}')
        print(f'Количество пройденых вариантов: {count_variant}')
        print(f'Время подбора составило: {time.time() - start_time}')
        break
    else:
        os.system('cls||clear')