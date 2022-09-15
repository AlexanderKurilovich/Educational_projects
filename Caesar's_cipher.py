# Шифр Цезаря
al = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']               
# Пользователь
print('Вам нужно зашифровать или дешифрование')
pl = input('Введите "+" если нужно зашифровать, введите "-" что бы расшифровать: ')
language = input('Введите язык который вам нужен Англиский(en) или Русский(ru): ')
if language == 'ru':
    language = 0
if language == 'en':
    language = 1
shift = int((pl + input('Введите число, шаг сдивга (шаг сдвига идет в право): ')))
text = input('Введите текст для обработки: ')
# Расшифровка или же зашифровка
for i in text:
    if i.isalpha():
        translation = al[language][(al[language].index(i.upper()) + shift) % len(al[language])]
        if i.isupper():
            print(translation, end='')
        else:
            print(translation.lower() ,end='')
    else:
        print(i, end='')