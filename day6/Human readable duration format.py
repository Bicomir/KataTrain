# -*- coding:utf-8 -*-

def format_duration(seconds):
    times = ['year', 'day', 'hour', 'minute', 'second']
    res = []
    result = ''
    if seconds == 0:
        return "now"
    else:
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)
        day , hour = divmod(hour, 24)
        year , day = divmod(day, 365)
        date = [year, day, hour, minute, second]
        for i,element in enumerate(date):
            if element:
                if element > 1:
                    times[i] += "s"
                res.append(str(element) + " " + times[i])
        length = len(res)
        result = ', '.join(res[:-1]) + ' and ' + res[length - 1] if length > 1 else res[0]
        return result

