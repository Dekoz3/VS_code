import numpy as np
    
def game_v3(number):
    '''Играем в детскую игру, после каждого ответа сужаем диапазон в 2 раза'''
    count=1
    max_range=100
    predict=max_range/2
    last_predict=0

    while number != predict: #цикл проверки условия и вычисления рамок диапазона
        count += 1
        if number > predict: #в случае если загаданное число больше нашей догадки
            last_predict=predict #переменная вводится для отсечения диапазона прошедшего проверку 
            predict = round((max_range + predict)/2)
        else: #в случае если загаданное число меньше нашей догадки
            max_range = predict
            predict = round((max_range+last_predict)/2)
    
    return(count)

def score_game(game_v3) -> int:
    """what is the mean quantity of tries computer guess the number , 1000 loops,
        выясняяем среднее количество попоток до выявления загаданного числа
    Args:
        random_predict (_type_): guessing function 
    

    Returns:
        int: mean quantity of tries среднее число попыток до выявления числа.
    """    
    count_ls = [] # список для сохранения количества попыток list to save quantity of tries
    np.random.seed(2) # фиксируем сид для воспроизводимости 
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел list of thinking numbers

    # for number in random_array:
    #     count_ls.append(game_v3(number)) # проходим по списку загаданных номеров функцией random_predict, получаем список количества попыток в каждом случае
    #     #taking main function game_v3() &  list of random numbers (random_array) having list of tries at the end of cycle
    # x = float()

    count_ls=[game_v3(x) for x in random_array]
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток mean number of tries to guess

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    print(f'''Your algorithm's mean number of tries is : {score}''')


    return(score)

# RUN
if __name__ == '__main__':
    score_game(game_v3)

