# Числовая угодайка
def pla():
    import random
    number = int(random.randint(1, 100))
    return number
print('Добро пожаловать в числовую угадайку')

def is_velid(n): # Футкция для проверки введенных дынных пользователем
    if 1 <= int(n) < 100:
        return True
    else:
        return False

def the_lawn(): # Функция ввода числа пользователя
    flag = False
    while flag != True:
        pl = input('Введите число от 1 до 100: ')
        if pl.isdigit():
            if  is_velid(pl) == True:
                    flag = True
                    if flag == True:
                        break        
            else:
                print('А может быть все-таки введем целое число от 1 до 100?')
                flag = False
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            flag = False
    return  int(pl)

def play():
    number = pla()
    counter = 1 # Счечик для потсчета попыток
    flag = False 
    while flag == False:
        pl = the_lawn()
        if number > pl:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
            flag = False
                
        elif number < pl:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
            flag = False
            
        elif number == pl:
            print('Вы угадали, поздравляем!')
            if counter == 1:
                print('Вы угадали за ', counter,' попытку' )
            elif 2 <= counter < 5:
                print('Вы угадали за ', counter,' попытки' )
            elif counter > 4:
                print('Вы угадали за ', counter,' попыток' )
            return  True

play()

flag_1 = False
while flag_1 == False:
    question = input('Хотите ли вы еще поиграть напишите "YES" что бы продолжить или же "NO" что бы закончить: ')
    if question == 'YES':
        play()
        continue
    elif question == 'NO':
        break
    
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')