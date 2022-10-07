start_day = int(input().split()[-1])

start_hour, start_minute, start_second = map(int, input().split(" : "))

start_time = start_day*24*60*60 + start_hour*60*60 + start_minute*60 + start_second

end_day = int(input().split()[-1])

end_hour, end_minute, end_second = map(int, input().split(" : "))

end_time = end_day*24*60*60 + end_hour*60*60 + end_minute*60 + end_second

time_dif = end_time - start_time

total_days = time_dif//(24*60*60)
time_dif = time_dif % (24*60*60)

total_hours = time_dif//(60*60)
time_dif = time_dif % (60*60)

total_minutes = time_dif // 60
time_dif = time_dif % 60

total_seconds = time_dif

print(f"{total_days} dia(s)")
print(f"{total_hours} hora(s)")
print(f"{total_minutes} minuto(s)")
print(f"{total_seconds} segundo(s)")