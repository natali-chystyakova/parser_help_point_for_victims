from django import template

register = template.Library()


@register.filter
def split_by_semicolon(value):
    """
    Делит строку по символу ';' и возвращает список.
    Если значение не строка, возвращает его без изменений.
    """
    if isinstance(value, str):
        return value.split(";")
    return value
