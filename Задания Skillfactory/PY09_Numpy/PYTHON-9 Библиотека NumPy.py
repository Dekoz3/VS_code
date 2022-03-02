import numpy as np
mystery_str=" 12279. -26024.  28745.     nan  31244.  -2365.  -6974.  -9212.     nan -17722.  16132.  25933.     nan -16431.  29810."
mystery_str.replace("  ", " ")
print(mystery_str)
mystery= np.array(list(mystery_str.split()), dtype=np.float32)
 
 # Получите булевый массив с информацией о np.nan в массиве mystery
# True - значение пропущено, False - значение не пропущено
print(mystery)

import numpy as np
nans_index = np.isnan(mystery)
print(nans_index)
# В переменную n_nan сохраните число пропущенных значений
n_nan = sum(lambda x: 1 for x in nans_index if nans_index is True)
print(n_nan)
# Заполните пропущенные значения в массиве mystery нулями



# Поменяйте тип данных в массиве mystery на int32



# Отсортируйте значения в массиве по возрастанию и сохраните
# результат в переменную array
array = None

# Сохраните в массив table двухмерный массив, полученный из массива array
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть
# по столбцам! Например, 1, 2, 3, 4 -> 1    3
#                                      2    4
table = None

#  Сохраните в переменную col средний столбец из table
col = None
