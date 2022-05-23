"""Game find number"""

import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count+=1
    pridict_number = int(input('Угадай число от 1 до 100: '))
    
    if pridict_number > number:
        print('Число должно быть меньше')
    elif pridict_number < number:
        print('Число должно быть больше')
    else:
        print(f'Вы угадали число {number} за {count} попыток.')
        break
    