money = int(input ('Введите сумму вклада:'))
per_cent = {'ТКБ': 5.6, 'СБК': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
rate = dict.values(per_cent)
deposit = [num/100*money for num in rate]
print("Максимальная сумма,которую вы можете заработать -", round(max(deposit)))