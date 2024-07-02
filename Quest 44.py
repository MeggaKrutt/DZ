# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd # добавил библиотеку пандас
import random
lst = ['robot'] * 10 # вписывает в переменную lst 10 значений robot
lst += ['human'] * 10 # прибавляет 10 значений human
random.shuffle(lst) # перемешивает список lst
data = pd.DataFrame({'whoAmI':lst}) # 1 столбец, заполняется перемешанными значениями из lst
print(data.head(), '\n') # отобразил, что получается в исходной задаче (5 строк)

data_2 = pd.DataFrame(columns=['robot', 'human']) # создаю новый DataFrame с двумя пустыми колонками
for i in range(len(lst)):   # заполняю новый датафрейм на основе значений первого датафрейма
    if lst[i] == 'robot':
        data_2.loc[i, 'robot'] = 1
        data_2.loc[i, 'human'] = 0
    else:
        data_2.loc[i, 'human'] = 1
        data_2.loc[i, 'robot'] = 0

print('Ответ:\n', data_2.head()) # вывел результат решения

# мои думалки как сделать:
# data_dict = {}
# data_dict['robot'] = 0
# data_dict['human'] = 1