#ex.2
time_in_sec = int(input("print time in seconds"))
time_hours = time_in_sec//3600
time_minutes = (time_in_sec-(time_in_sec//3600)*3600)//60
time_seconds = time_in_sec-(time_in_sec//3600)*3600-((time_in_sec-(time_in_sec//3600)*3600)//60)*60

print(f"{time_hours:02}:{time_minutes:02}:{time_seconds:02}")

