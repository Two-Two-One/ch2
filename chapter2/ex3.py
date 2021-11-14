now_time = input("Please enter the time now (in hours)")
total_time = int(now_time)

alarm_period = input("Please enter number of hours to wait for the alarm")
total_alarm = int(alarm_period)

secs_finally_remaining = (total_time+total_alarm)  % 24

print("Alarm time=", secs_finally_remaining)
