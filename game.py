''' Game guess the number'''
import numpy as np
number = np.random.randint(1, 101) # загадываем число, computer thingking the number
count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100 "))
    
    if predict_number > number:
        print("The number must be less")
        
    elif predict_number < number:
        print("The number must be lager")
    else:
        print(f"You guess the number! It's = {number}, You made {count} tries")
        break #The end of game, exit from cicle.

