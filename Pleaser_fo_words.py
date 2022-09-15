# Угодайка слов

import random

global word_list
word_list = ['Питон','Баскетбол','Волейбол','Геншин']

def get_word():
    result = random.choice(word_list).upper
    return result()
# Вскрытие буквы 
def Check_Letters(words, list):

   for i in words:
      if i in list:
         print(i, end=' ')
      else:
         print('_', end=' ')
   print()
# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def play(word):
   word_completion = '_ ' * len(word) # строка, содержащая символы _ на каждую букву задуманного слова
   guessed = False                    # сигнальная метка
   guessed_letters = []               # список уже названных букв
   guessed_words = []                 # список уже названных слов
   tries = 6                          # количество попыток
   
   print('Давайте играть в угадайку слов!')
   print(display_hangman(tries))
   print(word_completion)
   
   while True:
      pl = input('Введите букву или слово: ').upper()
      if not pl.isalpha():
         print('Можно вводить только буквы!')
         continue
      if pl in guessed_words or pl in guessed_letters:
         print("Это уже было")
      if len(pl) > 1:
         if pl == word:
            print("Поздровалю вы угодали слово!!!!!")
            break
         else:
            tries -= 1
            guessed_words.append(pl)
            print(display_hangman(tries))
            print(f'Не верно, у вас осталось попыток {tries}')
            if tries == 0:
               print(f'Вы не смогли угодать слова {word}')
               break
            continue
         
      if pl in word:
         guessed_letters.append(pl)
         if pl in word:
            if pl in word:
               print('Вы угадали букву')
               Check_Letters(pl, guessed_letters)
               continue
            if guessed:
               print(f"Вы смогли угодать слово, {word}")
               break
      else:
         guessed_letters.append(pl)
         tries -= 1
         print(display_hangman(tries))
         Check_Letters(word, guessed_letters)
         print(f'Не верно, у вас осталось попыток {tries}')
         if tries == 0:
            print(f'Вы не угадали слова {word}')
            break
         
         

print(play(get_word()))
