import os
import math

from django import template
from django.utils import timezone
from hurry.filesize import size

register = template.Library()

@register.filter()
def filename(value):
    try:
        return os.path.basename(value.file.name)
    except:
        return "NoFile!"

@register.filter()
def percentage(value, max):
    return round((value*100)/max)

@register.filter()
def rest_of_limit(value, max_file):
    res = max_file - value
    if res > 1024:
        return size(res)
    if res <= 1024:
        return size(1024)

@register.filter()
def byte_to_other(value, decimal_place=2):
    value = int(value)
    if value == 0:
        return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(value, 1024)))
    p = math.pow(1024, i)
    if decimal_place == 0:
        s = round(value / p)
    else:
        s = round(value / p, decimal_place)

    return "%s %s" % (s, size_name[i])

@register.filter()
def time_difference(value):
    now = timezone.now()
    difference = value - now

    times = {}
    times['days'] = difference.days
    times['minuts'] = round(difference.total_seconds()/60)
    times['hours'] = times['minuts'] / 60

    if 0 < times['days']:
        return f"{times['days']} Day"
    elif 1 <= times['hours'] <= 24:
        return f"{round(times['hours'])} Hour"
    elif 1 <= times['minuts'] <= 60:
        return f"{round(times['minuts'])} Minut"
