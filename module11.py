# first_name = input("Введите ваше имя:")
# last_name = input("Введите вашу фамилию:")
# age = input("Введите ваш возраст:")
# city = input("Введите город проживания:")
#
# # Выводим пустую строку
# print("")
#
# # Выводим приветствие, подставляя имя и фамилию пользователя,
# # которые он ввел с клавиатуры
# print("Привет,", first_name, last_name, "!")
#
# # Выводим пустую строку
# print("")
#
# # Выводим фиксированный текст для удобства просмотра
# print("Ваш профиль:")
#
# # Выводим возраст и город, которые указал пользователь
# print("Возраст:", age, 'лет')
# print("Город:", city)

# print (0.1+0.1*5-0.3*4)
#
# print(3 > 10)

# print (31 % 2 + 31 % 2)
#
# print (13 % 3 * 3 - 3**2)
#
# print(round(11*2.5/3, 2))
#
# print(round(11*2.5/3, 3))
#
# pi=3.14159
# print(round(pi**2/2))

# numbers = '1 2 3 4 5 6 7'
# numbers_split = numbers.split()
# numbers_joined = '\n'.join(numbers_split)
# print(numbers_joined)
#
# pi = 31.4159265
# print ("%.4e" % (pi))
#
# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[-1:-4:-1])
#
# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[-4::-1])

# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
#
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка



# # все операции - деление строки по пробелам, преобразование к числам
# # и приведение объекта map к типу список, можно делать в одной строке
# L = list(map(float, input().split()))
# # обмениваем первое и последнее число
# # с помощью множественного присваивания
# L[0], L[-1] = L[-1], L[0]
# # находим сумму и добавляем её в конец списка
# L.append(sum(L))
# print(L)

# d = {'day' : 22, 'month' : 6, 'year' : 2015}
# print("||".join(d.keys()))

# title = input('название книги: ')
# author = input('фамилия автора: ')
# year = int(input('год выпуска: '))
# book = {'title' : title, 'author' : author, 'year' : year}
# print(book)

# title = input('название книги: ')
# author = input('фамилия автора: ')
# year = input('год выпуска: ')
# year = int(year)
# book = {'title' : title, 'author' : author, 'year' : year}
# print(book)
#
# title = input('название книги: ')
# author = input('фамилия автора: ')
# year = input('год выпуска: ')
# book = {'title' : title, 'author' : author, 'year' : int(year)}
# print(book)

# text = input("Введите текст:")
# unique = list(set(text))
# print("Количество уникальных символов: ", len(unique))
#
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# a_set, b_set = set(a), set(b) # используем множественное присваивание
# a_and_b = a_set.symmetric_difference(b_set)
# print(a_and_b)

# L = ['a', 'b', 'c']
# print(id(L))
# L.append('d')
# print(id(L))


shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])
shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])
print(list_id_before == list_id_after)
print(list_id_before is list_id_after)