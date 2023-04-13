user = str(input("Введите ваш username: "))


def access(input_func):
    def output_func():
        if user == "admin":
            input_func()
        else:
            print("Доступ запрещен")
    return output_func


@access
def printing_cash():
    print("Сумма на счете: 20000$")


printing_cash()