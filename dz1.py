# Задание №1
print("№1")
while True:
    x = input("введите число или слово exit для выхода")
    len_x = 0
    s1 = 0
    s2 = 0
    if(x == "exit"):
        break

    for i in range(0, len(x)):
        if(x[i].isalpha() and x[i] != "-" and x != "."):
           print("введенное число не число" )
           len_x = 0
           break
        
        if(x[i] == "-"):
            s1 += 1
            if(s1 == 2):
                len_x = 0
                print("введенное число не число" )
                break
                break
            continue

        if(x[i] == "."):
            s2 += 1
            if(s2 == 2):
                len_x = 0
                print("введенное число не число" )
                break
                break
            continue

        len_x += 1

    if(len_x > 0):
        print("размер = ", len_x)





# Задание №2
print("№2")
while True:
    x = input("введите целочисленное число или слово exit для выхода")
    if(x == "exit"):
         break
    if(x.isdigit()):
        x = int(x)
    else: 
        print("введите целочисленное число")
        continue
    x_list = []
    x_plus = 0
    x_minus = 0
    for i in range(-x, x+1):
        x_list.append(i)
        if(i < 0):
            x_minus += i
        if(i > 0):
            x_plus += i
    print("Итоговый список = ", x_list)
    print("Сумма отрицательных = ", x_minus)
    print("Сумма положительных = ", x_plus)
        


# Задание №3
print("№3")
while True:
    x = input("введите число или слово exit для выхода")
    if(x == "exit"):
         break
    if(x.isdigit()):
        if(len(x) == 3):
            if(x[0] != x[1] and x[2] != x[0] and x[1] != x[2]):
                print(x[0],x[1],x[2])
                print(x[0],x[2],x[1])
                print(x[1],x[0],x[2])
                print(x[1],x[2],x[0])
                print(x[2],x[0],x[1])
                print(x[2],x[1],x[0])

            else: 
                print("есть повторяющиеся цифры")
        else: 
            print("размер не равен 3")
    else:
        print("не целочисленное число")


# Задание №4

#4.1)
print("№4.1")
while True:
    ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 И2К2"
    x = input("введите координату или слово exit для выхода").upper()

    if(len(x) <= 3 and len(x) >= 2):
        if("АБВГДЕЖЗИК".find(x[0]) >= 0 and "123456789".find(x[1]) >= 0 and len(x) == 2):
            print("попал" if ship.find(x) >= 0 else "мимо")
        elif("АБВГДЕЖЗИК".find(x[0]) >= 0 and "123456789".find(x[1]) >= 0 and len(x) == 3):
            if(x[2] == "0"):
                print("попал" if ship.find(x) >= 0 else "мимо")
            else: 
                print("3 символ не соответствует")
        else: 
            print("не соответсвует координате")

    if(x == "EXIT"):
        break


#4.2 п 1)
print("№4.2 п 1")
print("«Ваше имя: {0},  Фамилия: {1}, Возраст: {2} лет.»".format(input(), input(), input()))
input("нажмите Enter чтобы продолжить")

#4.2 п 2)
print("№4.2 п 2")
f_name = input()
s_name = input()
age = input()
print(f"«Ваше имя: {f_name},  Фамилия: {s_name}, Возраст: {age} лет.»")
input("нажмите Enter чтобы продолжить")


#В пункте 1 мы можем использовать только простые функции для изменения введенных данных, а в пункте 2 с полученными данными мы можем сделать что угодно.