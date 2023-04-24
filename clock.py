import os
import time
from datetime import datetime

current_time = datetime.now().time()
str_tn = current_time.strftime("%H:%M:%S")

def clear_screen():
    os.system("clear")     

num_0 = """ 
███████
██   ██
██   ██
██   ██
███████
"""
num_1 = """
     ██
  ██ ██
     ██
     ██
     ██
"""
num_2 = """
███████
    ███
  ███  
███    
███████
"""
num_3 = """
███████
     ██
███████
     ██
███████
"""
num_4 = """
██   ██
██   ██
███████
     ██
     ██
"""
num_5 = """
███████
██     
███████
     ██
███████
"""
num_6 = """
███████
██     
███████
██   ██
███████
"""

num_7 = """
███████
     ██
    ██ 
   ██  
  ██   
"""
num_8 = """
███████
██   ██
███████
██   ██
███████
"""
num_9 = """ 
███████
██   ██
███████
     ██
███████
"""
colon = """
  ███
  ███
     
  ███
  ███
"""
nothing = """
     
     
     
     
     
"""

clock_numbers = {
    "1": num_1,
    "2": num_2,
    "3": num_3,
    "4": num_4,
    "5": num_5,
    "6": num_6,
    "7": num_7,
    "8": num_8,
    "9": num_9,
    "0": num_0,
    ":": colon,
    "_": nothing
}


def clock_convert (time_string):
    num1 = None
    num2 = None
    if len(time_string) == 1:
        num1 = clock_numbers["0"]
        num2 = clock_numbers[time_string]
    else:
        num1 = clock_numbers[time_string[0]]
        num2 = clock_numbers[time_string[1]]
    return multilines_convert (num1, num2)


def multilines_convert (num1, num2):
    numbers = [f"{num1}  {num2}" for num1, num2 in zip (num1.splitlines(), num2.splitlines())]
    res = "\n".join(i for i in numbers)
    return res


def main():
    while True:
        clear_screen()
        current_time = datetime.now().time()
        str_tn = current_time.strftime("%H:%M:%S")
        hours = clock_convert(str_tn[:2])
        minutes = clock_convert(str_tn[3:5])
        seconds = clock_convert(str_tn[6:8])
        
        if int(str_tn[6:8])%2 == 0:
            clock = multilines_convert(hours, clock_numbers[":"])
        else:
            clock = multilines_convert(hours, clock_numbers["_"])
        clock = multilines_convert(clock, minutes)
        if int(str_tn[6:8])%2 == 0:
            clock = multilines_convert(clock, clock_numbers[":"])
        else:
            clock = multilines_convert(clock, clock_numbers["_"])
        clock = multilines_convert(clock, seconds)  
        print(clock)

        time.sleep(1)

main()