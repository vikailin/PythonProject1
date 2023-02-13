tickets = int(input('Введите количество необходимых билетов: '))
age_list = [int(input('Введите возраст посетителя: ')) for i in range(1, tickets+1)]
sum = 0
for age in age_list:
    if 0 < age < 18:
        sum += 0
    elif 18 <= age <= 25:
        sum += 990
    elif 25 < age < 100:
        sum += 1390
    else:
        print('Введено неверное значение возраста:', age)
if tickets > 3:
    discounted = sum - sum * 10//100
    print('Сумма к оплате с учетом скидки:', discounted)
else:
    print('Сумма к оплате:', sum)