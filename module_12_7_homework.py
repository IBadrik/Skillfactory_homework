#Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом,
#что ключ — название банка, значение — процент. Напишите программу, в результате которой будет
#сформирован список deposit значений — накопленные средства за год вклада в каждом из банков.
#На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.
#Добавьте в программу поиск максимального значения и его вывод на экран

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
per_cent_values = list(per_cent.values())
result = map(lambda num: num * money, per_cent_values)
deposit = list(result)
print(f'deposit = {deposit}')
print(f'Максимальная сумма, которую вы можете заработать - {max(deposit)}')

#Либо можно сделать так:
#per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#money = int(input())
#per_cent_values = list(per_cent.values())
#deposit = [value * money for value in per_cent_values]
#print(f'deposit = {deposit}')
#print(f'Максимальная сумма, которую вы можете заработать - {max(deposit)}')