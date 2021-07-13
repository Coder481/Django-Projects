from django import template
import datetime
register=template.Library()

@register.simple_tag
def get_date():
    now=datetime.datetime.now()
    return now

@register.filter
def quotes(value):
    s='"'+str(value)+'"'
    return s
