'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
'''

def timeConversion(s):
    h,m,s = s.split(":")
    s,day = s[:-2],s[-2:]
    if day == "PM":
        if h != "12":
            h = str(int(h)+12)
    else:   
        if h == "12":
            h = "00"
    return f"{h}:{m}:{s}"
