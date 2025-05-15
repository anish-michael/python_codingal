# 1hour = 3600 s
# 3610 s = 0 min 10 sec ---- 3610 // 3600 = 
# 3660s = 1 hour 1 min 0 sec ---- 3660 % 3600 = 60 => 60//60=1
# 70 s = 0 hour 1 min 10 sec ---- 70 % 60 = 10

total_seconds = int(input("enter time in seconds: "))
hours = total_seconds // 3600  #4.3 => 4
mins = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f'hours: {hours}, minutes: {mins}, seconds: {seconds}')