from django import template

register = template.Library()


@register.filter(name="myCut")
def myCut(value, arg):

    return value.replace(arg, "")


# register.filter("myCut", myCut)
