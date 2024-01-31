
'''Write a Python script that reads two integers, representing the hours (in the interval [0, 24[) and minutes (in the interval [0, 60[), using the 24-hour format and prints the equivalent hour in the 12-hour format.

The 12-hour clock is a time convention in which the 24 hours of the day are divided into two periods, "am" and "pm", each of 12 hours, numbered: 12 (acting as 0), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 and 11 (https://en.wikipedia.org/wiki/12-hour_clock).

The minutes are always represented with two digits and, If the minutes' value is zero, it should not appear in the output (see the examples).

If the hours and minutes values are incorrect, the script must print the message "INVALID DATE FORMAT".'''

hours = int(input())
minutes = int(input())

if (hours < 24 and minutes < 60):
    if hours < 12:
        period = "am" 
    else:
        period = "pm"
    
    if hours == 0:
        final_hours = 12
    elif hours <= 12:
        final_hours = hours
    else:
        final_hours = hours - 12
    
    if minutes == 0:
        print(str(final_hours) + " " + period)
    else:
        if minutes < 10:
            minutes_str = "0" + str(minutes)
        else:
            minutes_str = str(minutes)
        print(str(final_hours) + ":" + minutes_str + " " + period)
else:
    print("INVALID DATE FORMAT")