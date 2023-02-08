per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))
L = list(per_cent.values())
# deposit = [int(L[0]*money//100), int(L[1]*money//100), int(L[2]*money//100), int(L[3]*money//100)]
deposit = [L[0]*money//100, L[1]*money//100, L[2]*money//100, L[3]*money//100]
deposit = list(map(int, deposit))
print('deposit =', deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit))

