from django import template

register = template.Library()


def swap(data):
    return data.swapcase()


def remove(data,arg):
    ## return data.replace(arg,'')
    return data.replace(arg,'z')

def count(s, sub):
    c=0
    for i in range(len(s)):
        if s[i:i+len(sub)].lower()==sub:
            c+=1
    return c


register.filter('swapping',swap)
register.filter('removing',remove)
register.filter('counting',count)