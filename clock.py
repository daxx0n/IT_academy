import os
import time
from datetime import datetime
from colorama import init
from colorama import Fore
init()


num_0 = """
███████
██   ██
██   ██
██   ██
███████
"""
num_1 = """
   ██  
█████  
   ██  
   ██  
███████
"""
num_2 = """
███████
    ███
███████
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
colon1 = """
  ███
     
     
     
     
"""
colon2 = """
     
  ███
     
     
     
"""
colon3 = """
     
     
  ███
     
     
"""
colon4 = """
     
     
     
  ███
     
"""
colon5 = """
     
     
     
     
  ███
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
    ":1": colon1,
    ":2": colon2,
    ":3": colon3,
    ":4": colon4,
    ":5": colon5,
}

def clear_screen():
    os.system("clear")

# Convert time to string
def string_time(): 
    current_time = datetime.now().time()
    str_tn = current_time.strftime("%H:%M:%S")
    return str_tn

# Checking that time is not one digit
def clock_convert(str_time):
    num1 = None
    num2 = None
    if len(str_time) == 1:
        num1 = clock_numbers["0"]
        num2 = clock_numbers[str_time]
    else:
        num1 = clock_numbers[str_time[0]]
        num2 = clock_numbers[str_time[1]]
    return multilines_convert(num1, num2)

# Convert multilines to one string
def multilines_convert(num1, num2):
    numbers = [f"{num1}  {num2}" for num1, num2 in zip(
        num1.splitlines(), num2.splitlines())]
    res = "\n".join(i for i in numbers)
    return res

# Making analog clock from simple sistem clock
def clock():
    str_time = string_time()
    hours = clock_convert(str_time[:2])
    minutes = clock_convert(str_time[3:5])
    seconds = clock_convert(str_time[6:8])

    # realization of roling cube after hours:

    if int(str_time[7]) == 0 or int(str_time[7]) == 9:
        clock = multilines_convert(hours, clock_numbers[":1"])
    elif int(str_time[7]) == 1 or int(str_time[7]) == 8:
        clock = multilines_convert(hours, clock_numbers[":2"])
    elif int(str_time[7]) == 2 or int(str_time[7]) == 7:
        clock = multilines_convert(hours, clock_numbers[":3"])
    elif int(str_time[7]) == 3 or int(str_time[7]) == 6:
        clock = multilines_convert(hours, clock_numbers[":4"])
    elif int(str_time[7]) == 4 or int(str_time[7]) == 5:
        clock = multilines_convert(hours, clock_numbers[":5"])

    clock = multilines_convert(clock, minutes)

    # realization of roling cube after minutes:

    if int(str_time[7]) == 0 or int(str_time[7]) == 9:
        clock = multilines_convert(clock, clock_numbers[":1"])
    elif int(str_time[7]) == 1 or int(str_time[7]) == 8:
        clock = multilines_convert(clock, clock_numbers[":2"])
    elif int(str_time[7]) == 2 or int(str_time[7]) == 7:
        clock = multilines_convert(clock, clock_numbers[":3"])
    elif int(str_time[7]) == 3 or int(str_time[7]) == 6:
        clock = multilines_convert(clock, clock_numbers[":4"])
    elif int(str_time[7]) == 4 or int(str_time[7]) == 5:
        clock = multilines_convert(clock, clock_numbers[":5"])

    clock = multilines_convert(clock, seconds)
    return clock

# adding some colour to analog clock
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
        print(Fore.MAGENTA + clock_out)


def main():
    while True:
        clear_screen()
        color_output()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
