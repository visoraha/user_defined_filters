from django import template
register=template.Library()
@register.filter()
def swap(value):
    return value.swapcase()
#register.filter('swap',swap)

@register.filter()
def replace(value):
    return value.replace('a','')
#register.filter('replace',replace)

@register.filter()
def count(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:
            c+=1
    return c
#register.filter('count',count)