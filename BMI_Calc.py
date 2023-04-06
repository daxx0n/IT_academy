a = float(input("Введите Ваш рост в метрах (например - 1.86): "))
b = float(input("Введите Ваш вес в килограммах (например - 67): "))

s = [20]+["="]*15+[50] # 20 - minimal BMI, 50 - maximal BMI, one "=" - 2 points
bmi = round(b/(a**2), 2)
i = int(round((bmi-20)/2)) # position "|" in list, where 20 - minimal BMI
s[i] = "|" 

#here we must check that [i] is not negative, but "if" cannot be used, because we have not passed it yet. YAGNI :)

print ("Ваш индекс массы тела: ", bmi)
print (*s, sep="") 