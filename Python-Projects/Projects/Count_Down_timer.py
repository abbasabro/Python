import time as t

my_time = int(input("Enter the time in seconds : "))

for n in range(my_time , 0 ,-1):
    seconds = n % 60
    minutes = int(n / 60) % 60
    hours = int(n/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    t.sleep(1)
