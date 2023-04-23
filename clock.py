from datetime import datetime

current_time = datetime.now().time()


str_tn = current_time.strftime("%H:%M:%S")
print(str_tn)     