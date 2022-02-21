import numpy as np

def random_predict(number:int=1) -> int:
    """''' Game guess the number, Computer thinking the number and quessing it by itself
Игра угадай число. Компьютер сам загадывает и угадывает число


    Args:
        number (int, optional): Thinking the number. Defaults to 1.

    Returns:
        int: quantity of tries
    """''' '''
    count = 0
    # number = np.random.randint(1, 101) # загадываем число, computer thingking the number

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)
print(f'Quantity of tries {random_predict()}')


def score_game(random_predict) -> int:
    """what is the mean quantity of tries computer guess the number , 1000 loops,

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: mean quantity of tries
    """    
    count_ls = [] # список для сохранения количества попыток list to save quantity of tries
    np.random.seed(1) # фиксируем сид для воспроизводимости 
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел list of thinking numbers

    for number in random_array:
        count_ls.append(random_predict(number)) # проходим по списку загаданных номеров функцией random_predict, получаем список количества попыток в каждом случае

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
    
def game_core_v3(number):
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

score_game(game_core_v3)    