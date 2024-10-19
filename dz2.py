# # Задание №1
# # print("задание 1")
# x_str = input("данные через пробел ")
# x = list()
# x = x_str.split()
# x_x = input("степень = ")

# for i in range(len(x)):
#     try:
#         x[i] = float(x[i])**int(x_x)
#     except:
#         x[i] = x[i]*int(x_x)

# print(x)

# # Задание №2
# # print("задание 2")
# x_str = input("Введите строку ").lower()
# d = {}
# for i in range(len(x_str)):
#     if x_str[i] != " ":
#         d.update({ x_str[i] : x_str.count(x_str[i]) })
# print(d)

# # Задание №3
# # print("задание 3")
# dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
# k = set()
# v = set()
# for key, value in dct.items():
#     k.add(key)
#     v.add(value)
# print(k)
# print(v)
# print(k | v)

# # Задание №*"
# # print("задание *")
# dictionary = {
#     "Имя":                  ["Андрей", "Кирилл",    "Анна",     "Евгений",      "Евгений",      "Александр", "Татьяна",  "Аркадий", "Игорь", "Кирилл"],
#      "Фамилия":             ["Иванов", "Лазарев",   "Петрова",  "Надобников",   "Никитин",      "Иванов",    "Никитина", "Лихачев", "Никитин", "Левашев"],
#      "Город проживания":    ["Москва", "Омск",      "Псков",    "Псков",        "Москва",       "Псков",     "Москва",   "Омск",    "Псков", "Москва"],
#      "Год рождения":        [2000,      1987,    2003, 1993, 2001, 2001, 1976, 1957, 1969, 1999],
#      "Месяц рождения":      [6, 4, 11, 12, 9, 9, 5, 2, 3, 6],
#      "Число рождения":      [11, 25, 5, 3, 27, 31, 13, 12, 28, 24],
#      "Статус": ["Студент", "Работает", "Школьница", "Работает", "Студент", "Студент", "Работает", "Пенсия", "Работает", "Студент"]
# }
# # Вышел указ президента, который позволил имени «Кирилл» добавить еще одну «л» (Кириллл)
# # Семья Никитиных, живущая в Москве, переехала в Махачкалу
# # Иванов Александр закончил учебу и сейчас работает, а Лихачев Аркадий умер (убрать из словаря). Учитывать, что такие люди не имеют дубликатов по имени фамилии в словаре.
# ln = len(dictionary.get("Имя")) - 1
# i = 0

# while i <= ln:
#     if dictionary["Имя"][i] == "Кирилл": dictionary["Имя"][i] = "Кириллл"
#     if dictionary["Фамилия"][i].find("Никитин") >= 0 and dictionary["Город проживания"][i] == "Москва": dictionary["Город проживания"][i] = "Махачкала"
#     if dictionary["Имя"][i] == "Александр" and dictionary["Фамилия"][i] == "Иванов": dictionary["Статус"][i] = "Работает"
#     if dictionary["Имя"][i] == "Аркадий" and dictionary["Фамилия"][i] == "Лихачев":
#         for dp in (dictionary): dictionary[dp].remove(dictionary[dp][i])
#         ln -= 1
#         i -= 1
#     i += 1

# d = dict()
# d.update({ "Фамилия Имя" : [dictionary["Фамилия"][i] + " " + dictionary["Имя"][i] for i in range(len(dictionary["Имя"]))]})
# d.update({ "Дата рождения" : [str(dictionary["Год рождения"][i]) + "-" + str(dictionary["Месяц рождения"][i]) + "-" + str(dictionary["Число рождения"][i]) for i in range(len(dictionary["Имя"]))]})
# d.update({ "Город проживания" : [dictionary["Город проживания"][i] for i in range(len(dictionary["Город проживания"]))]})
# d.update({ "Статус" : [dictionary["Статус"][i] for i in range(len(dictionary["Статус"]))]})

# for dp in (d): print(d[dp])

# # Задание №*2"
# # print("задание *2")

# set1 = {6, 31, 14, 25, 19, 3, 55}
# set2 = {30, 22, 6, 79, 25}
# set3 = {9, 1, 22, 19, 30}

# set0 = set(zip(set1, set2))
# set0 = set(zip(set0, set3))

# print(set0)

# n2, n3 = zip(*set0)
# n1, n2 = zip(*n2)

# set1.symmetric_difference_update(n1)
# set2.symmetric_difference_update(n2)
# set3.symmetric_difference_update(n3)

# set_ = set1
# set_.update(set2)
# set_.update(set3)
# list_ = set_
# print(list_)