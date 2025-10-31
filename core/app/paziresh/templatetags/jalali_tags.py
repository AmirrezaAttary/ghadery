from django import template
import jdatetime

register = template.Library()

@register.filter
def to_jalali(value, fmt="%Y/%m/%d - %H:%M"):
    if not value:
        return ""
    try:
        j_date = jdatetime.datetime.fromgregorian(datetime=value)
        return j_date.strftime(fmt)
    except:
        return value
