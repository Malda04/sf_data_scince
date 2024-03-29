"""Game find number
Компьютер сам загадывает и сам угадыват число
"""

import numpy as np

def random_predict(number:int=1) ->int:
    """Рандомно угадываем число

    Args:
        namber (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    random_predict = np.random.randint(1, 101)
    count = 0
    min = 0 
    max = 100
    while True:
        predict = round((min+max)/2)
        count += 1
        if number == predict:
            break 
        elif number > predict:
            min = predict
            predict = round((max + min) / 2)
        elif number < predict:
            max = predict
            predict = round((max + min) / 2)

    return(count)

def score_game(random_predict) ->int:
    """За какое число попыток в среднем из 1000 подходов угадывает 
    наш алгоритм

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: среднее кол-во попыток
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)