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
    return (login)


def users_info():

    uinfo = {
        1: {"Рост": "180",
            "Вес": "120",
            "Шкала BMI": "20========|======50"},
        2: {"Рост": "150",
            "Вес": "80",
            "Шкала BMI": "20=======|=======50"},
        3: {"Рост": "190",
            "Вес": "54",
            "Шкала BMI": "20===============50"},
        4: {"Рост": "177",
            "Вес": "100",
            "Шкала BMI": "20=====|=========50"},
        5: {"Рост": "130",
            "Вес": "80",
            "Шкала BMI": "20=============|=50"}
    }
    return (uinfo)


def edit_users_info():
    uinfo = users_info()
    id = int(input("Введите id пользователя, которого вы хотите редактировать: "))
    print (uinfo[id])
    param = input(
        "Введите параметр, которые вы хотите отредактировать (Рост, Вес, Шкала BMI): ")
    value = input("Введите новое значение: ")
    uinfo[id][param] = value
    return uinfo[id]

def deleting_user():
    uinfo = users_info()
    id_del = int(input("Введите id пользователя, которого вы хотите удалить: "))
    del uinfo [id_del]
    return uinfo


def process_option(option):
    if option == "W":
        print(list_of_users())
    elif option == "I":
        id = int(input("Введите id пользователя: "))
        uinfo = users_info()
        print(uinfo[id])
    elif option == "E":
        print("Новые параметры: ", edit_users_info())
    elif option == "D":
        print("Оставшиеся пользователи: ", deleting_user())    


def main():
    # while option != "Q":
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
