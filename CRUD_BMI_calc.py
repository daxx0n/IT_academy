import os


def clear_screen():
    os.system("clear")


def print_menu_and_get_option():
    print("Добро пожаловать в калькулятор BMI!")
    print("Что бы вы хотели сделать?")
    print("1. Вывести список пользователей", "(W)")
    print("2. Посмотреть инфо о пользователе (рост, вес, шкала БМИ)", "(I)")
    print("3. Изменить данные о пользователе", "(E)")
    print("4. Удалить выбранного пользователя", "(D)")
    print("5. Добавить пользователя", "(A)")
    print("6. Выход", "(Q)")
    option = input("Введите свой выбор: ")
    clear_screen()
    return option


def list_of_users():
    login = {
        1: "Царь",
        2: "Царевич",
        3: "Король",
        4: "Королевич",
        5: "Сапожник"
    }
    return login


def users_info():
    uinfo = {
        1: {"Рост": "180",
            "Вес": "120",
            "Пол": "М",
            "Шкала BMI" : "20========|======50"},
        2: {"Рост": "150",
            "Вес": "80",
            "Пол": "Ж",
            "Шкала BMI" : "20=======|=======50"},
        3: {"Рост": "190",
            "Вес": "54",
            "Пол": "М",
            "Шкала BMI" : "20===============50"},
        4: {"Рост": "177",
            "Вес": "100",
            "Пол": "Ж",
            "Шкала BMI" : "20=====|=========50"},
        5: {"Рост": "130",
            "Вес": "80",
            "Пол": "М",
            "Шкала BMI" : "20=============|=50"}
    }
    return (uinfo)

def edit_users_info():
    uinfo = users_info()
    login = list_of_users()
    id = int(input("Введите id пользователя, которого вы хотите редактировать: "))
    print ("Имя: ", login [id])
    print ("Параметры:", uinfo[id])
    param = input(
        "Введите параметр, которые вы хотите редактировать (Рост, Вес, Пол, Шкала BMI): ")
    value = input("Введите новое значение: ")
    uinfo[id][param] = value
    return uinfo[id]

def deleting_user():
    uinfo = users_info()
    id = int(input("Введите id пользователя, которого вы хотите удалить: "))
    del uinfo [id]
    return uinfo

def adding_login():
    login = list_of_users()
    new_id = int(input ("Введите ваш ID: "))
    while (new_id in login):
        print("Введите другой ID, такой уже есть! ")
        new_id = int(input("Введите ваш ID: "))  
    new_login = input("Введите ваше имя: ")
    login[new_id] = new_login
    return login

def adding_parameters():
    uinfo = users_info()
    new_id = int(input ("Введите ваш ID: "))
    while (new_id in uinfo):
        print("Введите другой ID, такой уже есть! ")
        new_id = int(input("Введите ваш ID: ")) 
    heigh = float(input("Введите Ваш рост в метрах (например - 1.86): "))
    weight = float(input("Введите Ваш вес в килограммах (например - 67): "))
    sex = input("Введите ваш пол (М или Ж): ")
    s = [20]+["="]*15+[50] # 20 - minimal BMI, 50 - maximal BMI, one "=" - 2 points
    bmi = round(weight/(heigh**2), 2)
    if 20 <= bmi <= 50:
        i = int(round((bmi-20)/2)) # position "|" in list, where 20 - minimal BMI
        s[i] = "|"
    else:
        s = s
    uinfo[new_id] = {"Рост": heigh, "Вес": weight, "Пол": sex, "Шкала BMI": s}
    return uinfo


def process_option(option):
    if option == "W" or option == "1":
        print(list_of_users())
    elif option == "I" or option == "2":
        id = int(input("Введите id пользователя: "))
        uinfo = users_info()
        print(uinfo[id])
    elif option == "E" or option == "3":
        print("Новые параметры: ", edit_users_info())
    elif option == "D" or option == "4":
        print("Оставшиеся пользователи: ", deleting_user())   
    elif option == "A" or option == "5":
        new_login = adding_login()
        new_info = adding_parameters()
        id = int(input("Введите ID еще раз: "))
        print ("Ваш логин:", new_login[id])
        print ("Ваши параметры", new_info[id])


def main():
    option = print_menu_and_get_option()
    process_option(option)


main()

# 1. многопольз калькулятор БМИ(словарь) на 5 человек, шкалу тоже надо выводить
# 2. Храним рост, вес, пол,
# 3. Меню:CRUD(L)
#    1. Вывести список польз(ключ - login)(L)
#    2. Посмотреть инфо о пользователе (рост, вес, шкала БМИ) (R)
#    3. Изменить данные о пользователе (выбираем соот во ключу) (U)
#    4. Удалить выбранного пользователя (D)
#    5. Добавить пользователя(C)
#    6. Выход
