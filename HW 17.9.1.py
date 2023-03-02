num_list = list(map(int, input('Введите произвольную последовательность целых чисел через пробел: ').split()))
pointer = int(input('Введите случайное целое число, находящееся в пределах указанной Вами последовательности: '))


# функция сортировки пузырьком
def sort_num_list(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    return (f'Последовательность, сортированная в порядке возрастания чисел: {num_list}')


# функция линейного поиска
def find(num_list, pointer):
    for i, a in enumerate(num_list):
        if a == pointer:
            i = (i - 1)
            return i
    return False


if min(num_list) < pointer <= max(num_list):
    if pointer not in num_list:
        num_list.append(pointer)
    else:
        pass

    print(sort_num_list(num_list))
    print(find(num_list, pointer))

else:
    print('''Нарушено одно из условий ввода случайного числа!
    Условия:
    - введенное случайное число не должно быть больше максимального значения Вашей последовательности; 
    - введенное случайное число не должно быть меньше или равно минимальному значению Вашей последовательности.''')


