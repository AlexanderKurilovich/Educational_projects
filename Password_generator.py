# Генератор безопасных паролей
import random
 
print('Привет я генератор паролей ответь на на пару вопросов и я создам пароль')

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def  generate_password(length,content_1):
    content = content_1
    password = ''
    for _ in range(length):
        password += random.choice(content)
    return password

# Список  длинны паролей.
sp_password_length = []

# Количество паролей.
Number_of_passwords = int(input('Сколько надо создать паролей?: '))

for _ in range(Number_of_passwords):
    Password_length = int(input('Введите длинну одного из паролей:'))
    sp_password_length.append(Password_length)

# Содержание пароля.
sp_password_content = ""
for i in range(1):
    # Вопрос_1
    q1 = input('Хочешь чтобы твой пароль содержал цифры:"Yes" или "No" ') # q - вопрсы.
    if q1 == 'Yes':
        sp_password_content += digits
    else:
        print()
    # Вопрос_2
    q2 = input('Хочешь чтобы твой пароль содержал пропесные буквы:"Yes" или "No" ')
    if q2 == 'Yes':
        sp_password_content += uppercase_letters
    else:
        print()
    # Вопрос_3
    q3 = input('Хочешь чтобы твой пароль содержал строчный буквы:"Yes" или "No" ')
    if q3 == 'Yes':
        sp_password_content += lowercase_letters
    else:
        print()
    # Вопрос_4
    q4 = input('Хочешь чтобы твой пароль содержал символы:"Yes" или "No" ')
    if q4 == 'Yes':
        sp_password_content += punctuation
    else:
        print()
    break

for i in range(Number_of_passwords):
    print(i+1, 'пароль:', generate_password(sp_password_length[i], sp_password_content))