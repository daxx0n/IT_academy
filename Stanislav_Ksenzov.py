
a = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
print ("Шаг 1. Количество символов - ", len(a))
print ("Шаг 2. Развернутая строка - ", a[::-1])
print ("Шаг 3. Каждое слово с большой буквы - ", a.title())
print ("Шаг 4. Сделать весь текст прописными буквами - ", a.upper())
print ("Шаг 5. Количество вхождений в строку: 'нд' -", a.count("нд"), "'ам' -", a.count("ам"), "'о' -", a.count("о"))
print ("Шаг 6.1 Собственные упражнения - ", a.swapcase(), "- заглавные в строчные, а строчные в заглавные")
print ("Шаг 6.2 Собственные упражнения - ", a.lower(), "- все символы - строчные.")
print ("Шаг 6.3 Собственные упражнения - ", a.rfind("а"), "- индекс последнего вхождения символа 'а' в строке")

x = a.replace(",", " ,") # Для шага 7 корректнее будет сначала отделить знаки препинания, и только после этого делать реверс.
x1 = x.replace (".", " .")
x2 = x1.replace ("!", " !")

print ("Шаг 7. Развернуть строку - ", *x2.split()[::-1])
print ("Шаг 8. Вывести в консоль исходную строку - ", a)