import django.db.models
from django import template

register = template.Library()

censor_list = [
    'bla',
    'hell',
]


def word_censor(value):
    for pattern in censor_list:
        if value.lower().find(pattern) != -1:
            return value[0] + '*' * (len(value) - 1)
    return value


class censor_exception(Exception):
    def __str__(self):
        return 'Этот фильтр применяется только к строкам'


@register.filter()
def some_filter(value):
    return f'{value} use filter'


@register.filter()
def length_type(value, type):
    res = 0
    for obj in value:
        if obj.type == type:
            res += 1
    return res

@register.filter()
def censor(value):
    if isinstance(value, str):
        value = value.split(' ')
        result = ''
        for val in value:
            result += word_censor(val) + ' '
        return result.strip()
    else:
        raise censor_exception
