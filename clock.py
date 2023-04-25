import os
import time
from datetime import datetime
from colorama import init
init()
from colorama import Fore, Back, Style

def string_time():
    current_time = datetime.now().time()
    str_tn = current_time.strftime("%H:%M:%S")
    return str_tn
    
    
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


def clock_convert(time_string):
    num1 = None
    num2 = None
    if len(time_string) == 1:
        num1 = clock_numbers["0"]
        num2 = clock_numbers[time_string]
    else:
        num1 = clock_numbers[time_string[0]]
        num2 = clock_numbers[time_string[1]]
    return multilines_convert(num1, num2)


def multilines_convert(num1, num2):
    numbers = [f"{num1}  {num2}" for num1, num2 in zip(
        num1.splitlines(), num2.splitlines())]
    res = "\n".join(i for i in numbers)
    return res

def clock():
     str_time = string_time()
     hours = clock_convert(str_time[:2])
     minutes = clock_convert(str_time[3:5])
     seconds = clock_convert(str_time[6:8])
     if int(str_time[6:8]) % 2 == 0:
          clock = multilines_convert(hours, clock_numbers[":"])
     else:
          clock = multilines_convert(hours, clock_numbers["_"])
     clock = multilines_convert(clock, minutes)
     if int(str_time[6:8]) % 2 == 0:
          clock = multilines_convert(clock, clock_numbers[":"])
     else:
          clock = multilines_convert(clock, clock_numbers["_"])
     clock = multilines_convert(clock, seconds)
     return clock

def color_output():
     str_time = string_time()
     clock_out = clock()
     if int(str_time[7]) == 0 or int(str_time[7]) == 1:
          print(Fore.GREEN + clock_out)
     if int(str_time[7]) == 2 or int(str_time[7]) == 3:
          print(Fore.RED + clock_out)
     if int(str_time[7]) == 4 or int(str_time[7]) == 5:
          print(Fore.BLUE + clock_out)
     if int(str_time[7]) == 6 or int(str_time[7]) == 7:
          print(Fore.YELLOW + clock_out)
     if int(str_time[7]) == 8 or int(str_time[7]) == 9:
          print(Fore.MAGENTA+ clock_out)     

def main():
    while True:
        clear_screen()
        color_output()
        time.sleep(1)


main()
