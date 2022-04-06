# from collections import OrderedDict
# #ЗАДАНИЕ 3.2 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)
# #Дан список из кортежей temps. На первом месте в кортеже указан год в виде строки, а на втором — средняя температура января в Петербурге в указанном году.
# #Необходимо напечатать словарь, в котором ключи — годы, а значения — показатели температуры. Ключи необходимо отсортировать в порядке убывания соответствующих им температур.
# #Пример входа:

# temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]
# #Пример вывода:
# #OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])

# #temps=list(reversed(sorted(temps, key=lambda x: x[1])))

# print(temps)
# sort_temps=OrderedDict(list(reversed(sorted(temps, key=lambda x: x[1]))))

# print(sort_temps)

from collections import deque
def brackets(line):
    st=deque()
    for sign in line:
        if sign == "(":
            st.append(sign)
        else:
            try:
                st.pop()
            except IndexError:
                return False
    return st == deque([])


print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False